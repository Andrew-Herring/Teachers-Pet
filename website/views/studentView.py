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
  current_user = request.user
  print("CURRENT USER", current_user)
  student_list = Student.objects.filter(teacher_id=current_user.id)
  context = {'student_list' : student_list}
  template = 'website/students/student.html'
  return render(request, template, context)


# for adding a student to the classroom from the classroom details view
@login_required(login_url='/login')
def addStudent(request):
  if request.method == "GET":
    student_list = Student.objects.all
    skill_list = Skills.objects.all()
    course_list = Course.objects.all()
    context = {'student_list' : student_list, 'skill_list' : skill_list, 'course_list' : course_list}
    template = 'website/students/addStudent.html'
    return render(request, template, context)
  if request.method == "POST":
    firstName = request.POST['firstName']
    lastName = request.POST['lastName']
    email = request.POST['email']
    phone = request.POST['phone']
    nativeLanguage = request.POST['nativeLanguage']
    skillLevel = get_object_or_404(Skills, pk=request.POST['skillLevel'])
    speaking = get_object_or_404(Skills, pk=request.POST['speaking'])
    vocabulary = get_object_or_404(Skills, pk=request.POST['vocabulary'])
    reading = get_object_or_404(Skills, pk=request.POST['reading'])
    course = get_object_or_404(Course, pk=request.POST['courseSelect'])

    newStudent = Student(teacher = request.user.teacher, firstName = firstName, lastName = lastName, email = email, phone = phone, nativeLanguage = nativeLanguage, skillLevel = skillLevel, speaking = speaking, vocabulary = vocabulary, reading = reading)
    newStudent.save()
    newClassroom = Classroom(student = newStudent, course = course)
    newClassroom.save()
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
  student = get_object_or_404(Student, pk=student_id)
  skill_list = Skills.objects.all()
  context = {'student' : student, 'skill_list' : skill_list}
  template = 'website/students/studentEditForm.html'
  return render(request, template, context)


@login_required(login_url='/login')
def studentEdit(request, student_id):
  student = Student.objects.get(pk=student_id)
  # student.firstName = request.POST['firstName']
  # student.lastName = request.POST['lastName']
  # student.email = request.POST['email']
  # student.phone = request.POST['phone']
  # student.nativeLanguage = request.POST['nativeLanguage']
  student.skillLevel = get_object_or_404(Skills, pk=request.POST['skillLevel'])
  student.reading_id = get_object_or_404(Skills, pk=request.POST['reading'])
  student.speaking_id = get_object_or_404(Skills, pk=request.POST['speaking'])
  student.vocabulary_id = get_object_or_404(Skills, pk=request.POST['vocabulary'])
  student.save()
  return HttpResponseRedirect(reverse('website:studentDetails', args=(student.id,)))


@login_required(login_url="/login")
def studentDelete(request, student_id):
  student = get_object_or_404(Student, pk=student_id)
  student.delete()
  return HttpResponseRedirect(reverse("website:studentList"))

