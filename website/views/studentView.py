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
    reading = get_object_or_404(Skills, pk=request.POST ['reading'])
    newStudent = Student(firstName = firstName, lastName = lastName, email = email, phone = phone, nativeLanguage = nativeLanguage, skillLevel = skillLevel, speaking = speaking, vocabulary = vocabulary, reading = reading)
    newStudent.save()
    return redirect('website:studentList')  


@login_required(login_url='/login')
def studentDetails(request, id):
  studentDetails = get_object_or_404(Student, pk=id)
  student = Student.objects.filter(id=id)
  context = { 'studentDetails' : studentDetails, 'student' : student }
  template = 'website/students/studentDetails.html'
  return render(request, template, context)


@login_required(login_url='/login')
def studentEditForm(request, student_id):
  student = get_object_or_404(Student, pk = student_id)
  context = {'student' : student}
  return render(request, 'website/students/editStudent.html', context)


@login_required(login_url='/login')
def studentEdit (request, student_id):
  student = Student.objects.get(pk=student_id)
  student.firstName = request.POST['firstName']
  student.lastName = request.POST['lastName']
  student.email = request.POST['email']
  student.phone = request.POST['phone']
  student.nativeLanguage = request.POST['nativeLanguage']
  student.skillLevel = request.POST['skillLevel']
  student.reading_id = request.POST['reading_id']
  student.speaking_id = request.POST['speaking_id']
  student.vocabulary_id = request.POST['vocabulary_id']
  student.save()
  return redirect('website:studentDetails', args=(student.id))
