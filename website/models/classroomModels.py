from django.contrib.auth.models import User
from django.db import models
from .courseModels import Course
from .studentModels import Student


class Classroom(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)