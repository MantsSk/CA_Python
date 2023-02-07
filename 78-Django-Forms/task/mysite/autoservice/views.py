from django.shortcuts import render, get_object_or_404
from .forms import OrderReviewForm
from django.urls import reverse
from .models import Car, Service, Order
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin


def index(request):

    car_count = Car.objects.all().count()
    service_count = Service.objects.all().count()
    order_count = Order.objects.filter(status='d').count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'car_count': car_count,
        'service_count': service_count,
        'order_count': order_count,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


def cars(request):
    paginator = Paginator(Car.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    context = {
        'cars': paged_cars
    }

    return render(request, 'car_list.html', context=context)


def car(request, car_id):
    car = Car.objects.get(id=car_id)

    context = {
        'car': car
    }

    return render(request, 'car.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Car.objects.filter(
        Q(client__icontains=query) | Q(vin_code__icontains=query) | Q(car_make__model__icontains=query) | Q(license_plate__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})


class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    paginate_by = 2


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('order-detail', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad uzsakymas bus būtent tas, po kuriuo komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.order = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(
                        username=username, email=email, password=password)
                    messages.info(
                        request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')
