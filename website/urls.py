from django.conf.urls import url
from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
 
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    
    path('', views.index, name='index'),
    path('courses/', views.courseList, name ='courseList'),
    path('students/', views.studentList, name='studentList'),
]