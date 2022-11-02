from django.db import models

# Create your models here.
class Task(models.Model):
    heading = models.CharField(max_length=30)
    detail = models.CharField(max_length=40)
    date = models.DateField()
    is_deleted = models.CharField(max_length=2)
