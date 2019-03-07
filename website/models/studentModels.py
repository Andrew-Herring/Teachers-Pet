from django.contrib.auth.models import User
from django.db import models
from .skillModels import Skills

class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    nativeLanguage = models.CharField(max_length=100)
    skillLevel = models.ForeignKey(Skills, on_delete=models.CASCADE)