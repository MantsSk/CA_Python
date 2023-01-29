from django.db import models

# Create your models here.


class CarMake(models.Model):
    make = models.CharField('Make', max_length=20,
                            help_text='Car make', null=False)
    model = models.CharField('Model', max_length=20,
                             help_text='Car model', null=False)

    def __str__(self):
        return f'{self.make} {self.model}'


class Car(models.Model):
    license_plate = models.CharField(
        'Licence plate', max_length=10, help_text='Car\'s licence plate', null=False)
    car_make = models.ForeignKey(
        'CarMake', on_delete=models.CASCADE, null=False)
    vin_code = models.CharField(
        'Vin code', max_length=20, help_text='Car\'s vin code', null=False)
    client = models.CharField('Client', max_length=50,
                              help_text='Client\'s name', null=False)

    def __str__(self):
        return f'{self.car_make} ({self.license_plate})'


class Order(models.Model):
    date = models.DateField('Date', help_text='Order\'s date', null=False)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.car} ({self.date})'


class Service(models.Model):
    title = models.CharField(
        'Title', help_text='Title of the service', max_length=50, null=False)
    price = models.FloatField('Price', help_text='The price of the service')

    def __str__(self):
        return f'{self.title} ({self.price})'


class OrderService(models.Model):
    service = models.ForeignKey(
        'Service', on_delete=models.CASCADE, null=False)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(
        'Quantity', help_text='Quantity of the service', null=False)

    def __str__(self):
        return f'{self.service} ({self.order}x{self.quantity})'
