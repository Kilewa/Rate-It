from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home,name='rateapp-home'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
    url('^uploads/',views.post_site,name='post_site'),
    url(r'^api/profiles/$', views.ProfileList.as_view(),name='profile_list'),
    url(r'^api/projects/$', views.ProjectsList.as_view(),name='projects_list'),
    url(r'^search/', views.search_results, name='search_results'),
]