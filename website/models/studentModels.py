from django.contrib.auth.models import User
from django.db import models
from .skillModels import Skills
from .teacherModels import Teacher

class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    nativeLanguage = models.CharField(max_length=100)
    speaking = models.ForeignKey(Skills, related_name='speaking', on_delete=models.CASCADE)
    reading = models.ForeignKey(Skills, related_name='reading', on_delete=models.CASCADE)
    vocabulary = models.ForeignKey(Skills, related_name='vocabulary', on_delete=models.CASCADE)
    skillLevel = models.ForeignKey(Skills, related_name='skillLevel', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
