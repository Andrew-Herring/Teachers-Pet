from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.urls import reverse


from website.models.classroomModels import Classroom
from website.models.teacherModels import Teacher
from website.models.skillModels import Skills
from website.models.courseModels import Course
from website.models.studentModels import Student

# get a complete list of students, access through the navbar or /students
@login_required(login_url='/login')
def studentList(request):
  student_list = Student.objects.all()
  context = {'student_list' : student_list}
  template = 'website/students/student.html'
  return render(request, template, context)


# for adding a student to the classroom from the classroom details view
@login_required(login_url='/login')
def addStudent(request):
  if request.method == "GET":
    student_list = Student.objects.all
    skill_list = Skills.objects.all()
    context = {'student_list' : student_list, 'skill_list' : skill_list}
    template = 'website/students/addStudent.html'
    return render(request, template, context)
  if request.method == "POST":
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    phone = request.POST['phone']
    nativeLanguage = request.POST['nativeLanguage']
    skillLevel = get_object_or_404(Skills, pk=request.POST['skillLevel'])
    speaking = get_object_or_404(Skills, pk=request.POST ['speaking'])
    vocabulary = get_object_or_404(Skills, pk=request.POST ['vocabulary'])
    writing = get_object_or_404(Skills, pk=request.POST ['writing'])
    newStudent = Student(firstName = firstName, lastName = lastName, email = email, phone = phone, nativeLanguage = nativeLanguage, skillLevel = skillLevel, speaking = speaking, vocabulary = vocabulary, writing = writing)
    newStudent.save()
    return redirect('website:studentList')  