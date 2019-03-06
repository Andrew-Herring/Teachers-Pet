from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Product(models.Model):
#     seller = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#     )
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.IntegerField()
#     quantity = models.IntegerField()

class Teacher(models.Model):
    languages = models.CharField(max_length=50)
    phone = IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)


class Course(models.Model):
    level = models.CharField(max_length=2)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher)


class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    nativeLanguage = models.CharField(max_length=100)
    skillLevel = models.ForeignKey(Skills)


class Skills(models.Model):
    level = models.CharField(max_length=2)


class Classroom(models.Model):
    startDate = models.DateField()
    endDate = models.Datefield()
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)