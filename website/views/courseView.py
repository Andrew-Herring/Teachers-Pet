from django.shortcuts import render, get_object_or_404, redirect
from website.models.courseModels import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from website.models.studentModels import Student
from website.models.classroomModels import Classroom
from website.models.teacherModels import Teacher
from website.models.skillModels import Skills
from website.models.courseModels import Course

@login_required(login_url='/login')
def courseList(request):
  course_list = Course.objects.all()
  template = 'website/courses/courses.html'
  return render(request, template, {'courses' : course_list})

@login_required(login_url='/login')
def addCourse(request):
  if request.method == "GET":
    teacher_list = Teacher.objects.all()
    course_list = Course.objects.all()
    skill_list = Skills.objects.all()
    template = 'website/courses/addCourse.html'
    context = {'courses' : course_list, 'skill_list' : skill_list, 'teacher_list' : teacher_list}
    return render(request, template, context)

  if request.method == "POST":
    location = request.POST['location']
    time = request.POST['time']
    days = request.POST['days']
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']
    level = get_object_or_404(Skills, pk=request.POST['level'])
    teacher = request.user.teacher
    newCourse = Course(location = location, time = time, days = days, startDate = startDate, endDate = endDate, level = level, teacher = teacher)
    newCourse.save()
    return redirect('website:courseList')

@login_required(login_url='/login')
def courseDetails(request, course_id):
  courseDetails = get_object_or_404(Classroom, pk=course_id)
  classroom = Classroom.objects.filter(course_id=course_id)
  # print("my students", students)
  context = { 'courseDetails' : courseDetails, 'classroom' : classroom }
  template = 'website/classroom/courseDetails.html'
  return render(request, template, context)
