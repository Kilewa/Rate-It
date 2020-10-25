from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
from django.core.validators import MaxValueValidator
from url_or_relative_url_field.fields import URLOrRelativeURLField
from tinymce.models import HTMLField


class Projects(models.Model): 
    profile = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 
    title = models.CharField(max_length=20,blank=True)
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    image_landing = models.ImageField(upload_to='landing/')
    description = HTMLField(max_length=200,blank=True)
    link = URLOrRelativeURLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    @classmethod
    def search_by_projects(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        print(projects)
        return projects 
    
    @classmethod
    def get_profile_projects(cls,profile):
        projects = Projects.objects.filter(profile__pk=profile)
        print(projects)
        return projects
    
    
    def __str__(self):
        return self.title
    

class Rates(models.Model):
    design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)]) 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.IntegerField(default=0) 


class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField(max_length=400)     
    pro_id = models.IntegerField(default=0) 