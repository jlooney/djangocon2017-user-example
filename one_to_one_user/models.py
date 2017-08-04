from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.TextField(max_length=50, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    fav_pokemon = models.CharField(max_length=1000, null=True, blank=True)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


'''
This is necessary if you are adding the Profile attributes in the admin.
Both the django admin save and the post_save will trigger when you save in the admin,
so you want to check to make sure it doesn't get saved twice.
'''
def save(self, *args, **kwargs):
    if not self.pk:
        try:
            p = Profile.objects.get(user=self.user)
            self.pk = p.pk
        except Profile.DoesNotExist:
            pass

    super(Profile, self).save(*args, **kwargs)