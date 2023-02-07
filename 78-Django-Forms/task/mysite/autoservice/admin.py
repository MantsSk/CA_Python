from django.contrib import admin
from .models import CarMake, Car, Order, OrderService, Service, OrderReview


class CarAdmin(admin.ModelAdmin):
    search_fields = ('license_plate', 'vin_code')
    list_filter = ('client', 'car_make__model')
    list_display = ('car_make', 'client', 'license_plate', 'vin_code')


class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order', 'date_created', 'reviewer', 'content')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


class OrderServiceInstanceInline(admin.TabularInline):
    model = OrderService
    extra = 0
    can_delete = False


class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'car')
    inlines = [OrderServiceInstanceInline]


admin.site.register(Car, CarAdmin)
admin.site.register(CarMake)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderService)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderReview, OrderReviewAdmin)
# Register your models here.
