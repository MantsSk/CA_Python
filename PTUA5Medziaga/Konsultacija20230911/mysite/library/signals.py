from django.db.models.signals import post_save  # signalas (būna įvairių)
from django.contrib.auth.models import User     # siuntėjas
from django.dispatch import receiver            # priėmėjas (dekoratorius)
from .models import Profile


# Sukūrus vartotoją automatiškai sukuriamas ir profilis.
# jeigu išsaugojamas User objektas, inicijuojama f-ja po dekoratoriumi
@receiver(post_save, sender=User)
# instance yra ką tik sukurtas User objektas.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('KWARGS: ', kwargs)


# Pakoregavus vartotoją, išsaugomas ir profilis
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
