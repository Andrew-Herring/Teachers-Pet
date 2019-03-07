from django.shortcuts import render, get_object_or_404
from website.models.courseModels import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from website.models.courseModels import Course


def courseList(request):
  course_list = Course.objects.all()
  template = 'website/courses/courses.html'
  return render(request, template, {'courses' : course_list})