from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import GameReviewForm
from .models import GameReview, Publisher, Game
from django.views import generic
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin


def index(request):
    review = GameReview.objects.latest('id')

    context = {
        'review': review
    }

    return render(request, "index.html", context)


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.success(request, f'Vartotojas {username} prisijunge')
                    return redirect('index')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')


class PublisherView(generic.ListView):
    model = Publisher
    template_name = "publishers.html"
    paginate_by = 3

def publisher(request, publisher_id):
    single_publisher = get_object_or_404(Publisher, pk=publisher_id)
    return render(request, 'publisher.html', {'publisher': single_publisher})


class GameListView(generic.ListView):
    model = Game
    template_name = 'games.html'


class GameDetailView(FormMixin, generic.DetailView):
    model = Game
    template_name = 'game.html'
    form_class = GameReviewForm
    

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('game', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.game = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(GameDetailView, self).form_valid(form)
