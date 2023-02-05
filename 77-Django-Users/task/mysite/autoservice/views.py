from django.shortcuts import render
from .models import Car, Service, Order
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


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


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
