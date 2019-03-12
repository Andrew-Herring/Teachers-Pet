from django.contrib.auth.models import User
from django.db import models
from .teacherModels import Teacher
from .skillModels import Skills


class Course(models.Model):
    level = models.ForeignKey(Skills, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    time = models.CharField(max_length=10)
    days = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

