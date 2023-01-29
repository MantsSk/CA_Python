from django.contrib import admin
from .models import CarMake, Car, Order, OrderService, Service

admin.site.register(Car)
admin.site.register(CarMake)
admin.site.register(Order)
admin.site.register(OrderService)
admin.site.register(Service)
