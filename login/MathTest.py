from django.db import models


class math_test(models.Model):
    which_angel = models.CharField(max_length=40)
    total = models.CharField(max_length=10)
