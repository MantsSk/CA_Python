from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class CarMake(models.Model):
    make = models.CharField('Make', max_length=20,
                            help_text='Car make', null=False)
    model = models.CharField('Model', max_length=20,
                             help_text='Car model', null=False)

    def __str__(self):
        return f'{self.make} {self.model}'

    class Meta:
        verbose_name = 'Car make'
        verbose_name_plural = 'Car makes'


class Car(models.Model):
    license_plate = models.CharField(
        'Licence plate', max_length=10, help_text='Car\'s licence plate', null=False)
    car_make = models.ForeignKey(
        'CarMake', on_delete=models.CASCADE, null=False)
    vin_code = models.CharField(
        'Vin code', max_length=20, help_text='Car\'s vin code', null=False)
    client = models.CharField('Client', max_length=50,
                              help_text='Client\'s name', null=False)
    image = models.ImageField(
        'Image', upload_to='car_images', null=True)

    def __str__(self):
        return f'{self.car_make} ({self.license_plate})'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Order(models.Model):
    date = models.DateField('Date', help_text='Order\'s date', null=False)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=False)

    STATUS = (
        ('o', 'Ordered'),
        ('i', 'In progress'),
        ('d', 'Done')
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='o',
        help_text='Status',
    )

    @property
    def sum(self):
        order_services = OrderService.objects.filter(order=self.id)
        sum = 0
        for order_service in order_services:
            sum += order_service.sum
        return sum

    def __str__(self):
        return f'{self.car} ({self.date})'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderReview(models.Model):
    order = models.ForeignKey(
        'Order', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField('Review', max_length=2000)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = 'Reviews'
        ordering = ['-date_created']


class Service(models.Model):
    title = models.CharField(
        'Title', help_text='Title of the service', max_length=50, null=False)
    price = models.FloatField('Price', help_text='The price of the service')

    def __str__(self):
        return f'{self.title} ({self.price})'

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class OrderService(models.Model):
    service = models.ForeignKey(
        'Service', on_delete=models.CASCADE, null=False)
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(
        'Quantity', help_text='Quantity of the service', null=False)

    @property
    def sum(self):
        return self.quantity * self.service.price

    def __str__(self):
        return f'{self.service} ({self.order}x{self.quantity})'

    class Meta:
        verbose_name = 'Order service'
        verbose_name_plural = 'Order services'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        default="profile_pics/default.jpeg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
