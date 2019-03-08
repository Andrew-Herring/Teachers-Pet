from django.shortcuts import render, get_object_or_404
from website.models.courseModels import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required



from website.models.courseModels import Course

@login_required(login_url='/login')
def courseList(request):
  course_list = Course.objects.all()
  template = 'website/courses/courses.html'
  return render(request, template, {'courses' : course_list})


def addCourse(request):
  if request.method == "GET":
    course_list = Course.objects.all()
    template = 'website/courses/addCourse.html'
    return render(request, template, {'courses' : course_list})
  if request.method == "POST":
    location = request.POST['location']
    time = request.POST['time']
    days = request.POST['days']
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']
    level = request.POST['level']
    newCourse = Course(location = location, time = time, days = days, startDate = startDate, endDate = endDate, level = level)
    newCourse.save()
    response = redirect('website:courseList')
    return response

