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
  return render(request, template, {'course_list' : course_list})

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
  print("DETAILS", course_id)
  courseDetails = get_object_or_404(Course, pk=course_id)
  # classroom = Classroom.objects.filter(course_id=course_id)
  # print("my students", students)
  context = { 'courseDetails' : courseDetails }
  template = 'website/classroom/courseDetails.html'
  return render(request, template, context)

@login_required(login_url='/login')
def courseEditForm(request, course_id):
  course = get_object_or_404(Course, pk=course_id)
  skill_list = Skills.objects.all()
  context = {'course' : course, 'skill_list' : skill_list}
  template = 'website/courses/courseEditForm.html'
  return render(request, template, context)

@login_required(login_url='/login')
def courseEdit(request, course_id):
  course = Course.objects.get(pk=course_id)
  course.location = request.POST['location']
  course.time = request.POST['time']
  course.days = request.POST['days']
  # course.startDate = request.POST['startDate']
  # course.endDate = request.POST['endDate']
  course.level = get_object_or_404(Skills, pk=request.POST['level'])
  course.teacher = request.user.teacher
  course.save()
  return HttpResponseRedirect(reverse('website:courseDetails', args=(course.id,)))

@login_required(login_url="/login")
def courseDelete(request, course_id):
  course = get_object_or_404(Course, pk=course_id)
  course.delete()
  return HttpResponseRedirect(reverse("website:courseList"))