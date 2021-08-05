from django.db import models
from datetime import date
# Create your models here.


class ActivityReport(models.Model):
    username = models.CharField(max_length=240, default=" ")
    branch = models.CharField(max_length=240, default=" ")
    areas = models.CharField(max_length=240, default=" ")
    title = models.CharField(max_length=240, default=" ")
    location = models.CharField(max_length=240, default=" ")
    date = models.DateField(default=date.today)
    duration = models.CharField(max_length=240, default=" ")
    participants = models.CharField(max_length=240, default=" ")
    materials = models.TextField()
    goals = models.TextField()
    description = models.TextField()
    strengths = models.TextField()
    weaknesses = models.TextField()
    improvements = models.TextField()
    def __str__(self):
        return self.title
