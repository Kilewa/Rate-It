from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home,name='rateapp-home'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
]