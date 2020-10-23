from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        '''
        Saves profile instance to db
        '''
        self.save()

    @classmethod
    def get_all_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def get_profile_by_user_id(cls, userid):
        '''
        Returns profile based on user id
        '''
        profile = cls.objects.get(user=userid)
        return profile

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)