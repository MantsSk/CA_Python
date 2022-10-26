from django.db.models.signals import post_save  # signalas (būna įvairių)
from django.contrib.auth.models import User     # siuntėjas
from django.dispatch import receiver            # priėmėjas (dekoratorius)
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()