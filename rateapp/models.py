from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile


class Post(models.Model):
    image = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)
    caption = models.CharField(max_length=100, default='')
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.image_name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

