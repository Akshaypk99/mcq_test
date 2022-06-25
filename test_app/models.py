from django.db import models

# Create your models here.
from django.contrib.auth.models import User
User._meta.get_field('email').blank = False

class Task(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Correct_ans = models.CharField(max_length=100)

    