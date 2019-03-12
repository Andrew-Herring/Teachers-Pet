from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from website.models.studentModels import Student

@login_required(login_url='/login')
def studentList(request):
  student_list = Student.objects.all()
  template = 'website/students/student.html'
  return render(request, template, {'students' : student_list})

@login_required(login_url='/login')
  def addStudent(request):
    