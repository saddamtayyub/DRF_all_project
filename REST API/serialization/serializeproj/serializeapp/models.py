from django.db import models


# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    city = models.CharField(max_length=200)
