from django.dispatch import receiver
from django.db.models.signals import post_save
from relationship_app.models import UserProfile, User

@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])
    