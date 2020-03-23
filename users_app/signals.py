from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


def create_profile(sender, instance, **kwargs):
    try:
        Profile.objects.get(user_id=instance.id)
    except ObjectDoesNotExist:
        new_profile = Profile()
        new_profile.user = instance
        new_profile.save()