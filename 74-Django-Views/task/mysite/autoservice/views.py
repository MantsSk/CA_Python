from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Service, Order
from django.views import generic


def index(request):

    car_count = Car.objects.all().count()
    service_count = Service.objects.all().count()
    order_count = Order.objects.filter(status='d').count()

    context = {
        'car_count': car_count,
        'service_count': service_count,
        'order_count': order_count,
    }

    return render(request, 'index.html', context=context)


def cars(request):
    cars = Car.objects.all()

    context = {
        'cars': cars
    }

    return render(request, 'car_list.html', context=context)


def car(request, car_id):
    car = Car.objects.get(id=car_id)

    context = {
        'car': car
    }

    return render(request, 'car.html', context=context)


class OrderListView(generic.ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
