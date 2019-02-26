from django.db import models


# Create your models here.

class homework(models.Model):
    which_angel = models.CharField(max_length=30, unique = True)
    total = models.CharField(max_length=4)
    right = models.CharField(max_length=4)
    wrong = models.CharField(max_length=4)
    list = models.CharField(max_length=1000)
    subject = models.CharField(max_length=10)


class math_test(models.Model):
    which_angel = models.CharField(max_length=40)
    total = models.CharField(max_length=10)


class math(models.Model):
    which_angel = models.CharField(max_length=40)
    total = models.CharField(max_length=10)
