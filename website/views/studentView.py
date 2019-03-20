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
  # get current user to show students specific to the logged in user
  current_user = request.user
  # grab a list of students that belong to the teacher
  student_list = Student.objects.filter(teacher_id=current_user.id)
  # set student list as a dictionary
  context = {'student_list' : student_list}
  # html template
  template = 'website/students/student.html'
  return render(request, template, context)


# add a student and assign them to a class
@login_required(login_url='/login')
def addStudent(request):
  # if the method is get...
  if request.method == "GET":
    # logged in users create students only they can see
    current_user = request.user
    # list all of a teachers' students
    student_list = Student.objects.filter(teacher_id=current_user.id)
    # get all skill values from the skills table to put them into the dropdowns
    skill_list = Skills.objects.all()
    # user assigns new student to one of their courses
    course_list = Course.objects.filter(teacher_id=current_user.id)
    # create dictionaries for the data
    context = {'student_list' : student_list, 'skill_list' : skill_list, 'course_list' : course_list}
    # html template
    template = 'website/students/addStudent.html'
    return render(request, template, context)
    # if the method is post....
  if request.method == "POST":
    # take values from the form the user fills out and assign the value to a variable
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
    # create the new student with the provided values
    newStudent = Student(teacher = request.user.teacher, firstName = firstName, lastName = lastName, email = email, phone = phone, nativeLanguage = nativeLanguage, skillLevel = skillLevel, speaking = speaking, vocabulary = vocabulary, reading = reading)
    # save the newly constructed student
    newStudent.save()
    # create a new entry on the classroom table that joins courses and students together
    newClassroom = Classroom(student = newStudent, course = course)
    # save the new classroom data
    newClassroom.save()
    # return the user to the student list
    return redirect('website:studentList')  


@login_required(login_url='/login')
def studentDetails(request, id):
  # get a specific student from the Student table
  studentDetails = get_object_or_404(Student, pk=id)
  student = Student.objects.filter(id=id)
  context = { 'studentDetails' : studentDetails, 'student' : student }
  template = 'website/students/studentDetails.html'
  return render(request, template, context)


@login_required(login_url='/login')
def studentEditForm(request, student_id):
  # retrieve students data to fill the forms with
  student = get_object_or_404(Student, pk=student_id)
  # fetch skill data to populate dropdowns
  skill_list = Skills.objects.all()
  context = {'student' : student, 'skill_list' : skill_list}
  template = 'website/students/studentEditForm.html'
  return render(request, template, context)


@login_required(login_url='/login')
def studentEdit(request, student_id):
  # rewrite student values
  student = Student.objects.get(pk=student_id)
  student.skillLevel = get_object_or_404(Skills, pk=request.POST['skillLevel'])
  student.reading_id = get_object_or_404(Skills, pk=request.POST['reading'])
  student.speaking_id = get_object_or_404(Skills, pk=request.POST['speaking'])
  student.vocabulary_id = get_object_or_404(Skills, pk=request.POST['vocabulary'])
  student.save()
  return HttpResponseRedirect(reverse('website:studentDetails', args=(student.id,)))


@login_required(login_url="/login")
def studentDelete(request, student_id):
  # remove a student from the student table
  student = get_object_or_404(Student, pk=student_id)
  student.delete()
  return HttpResponseRedirect(reverse("website:studentList"))

