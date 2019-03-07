from django.contrib.auth.models import User
from django.db import models

class Teacher(models.Model):
  languages = models.CharField(max_length=50)
  phone = models.IntegerField()
  user = models.OneToOneField(User, on_delete=models.PROTECT)