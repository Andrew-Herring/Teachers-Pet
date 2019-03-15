from django.conf.urls import url
from django.urls import path

from . import views

app_name = "website"
urlpatterns = [
    #Auth URL's 
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    
    path('', views.index, name='index'),
    # Course URL's
    path('courses/', views.courseList, name ='courseList'),
    path('courseDetails/<int:course_id>', views.courseDetails, name ='courseDetails'),
    # Student URL's
    path('addCourse/', views.addCourse, name ='addCourse'),
    path('students/', views.studentList, name='studentList'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('studentDetails/<int:id>', views.studentDetails, name='studentDetails'),
    path('studentEdit/<int:student_id>', views.studentEdit, name='studentEdit'),
    path('studentEditForm/<int:student_id>', views.studentEditForm, name='studentEditForm')
]