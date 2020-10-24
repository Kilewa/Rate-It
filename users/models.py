from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    bio = HTMLField(max_length=300,default="No bio")
    profile_photo = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    website = URLOrRelativeURLField(default='')     

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

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  