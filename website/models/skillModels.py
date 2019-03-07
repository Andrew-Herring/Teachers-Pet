from django.contrib.auth.models import User
from django.db import models

class Skills(models.Model):
    level = models.CharField(max_length=2)