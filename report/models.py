from django.db import models

# Create your models here.


class Report(models.Model):
    username = models.CharField(max_length=40, default=" ")
    title = models.CharField(max_length=40, default=" ")
    location = models.CharField(max_length=40, default=" ")
    duration = models.CharField(max_length=40, default=" ")
    date = models.DateField()
    participants = models.CharField(max_length=40, default=" ")
    branch = models.CharField(max_length=40, default=" ")
    areas = models.CharField(max_length=140, default=" ")
    goals = models.CharField(max_length=40, default=" ")
    description = models.CharField(max_length = 1000)
    strengths = models.TextField()
    weaknesses = models.TextField()
    improvements = models.TextField()
    def __str__(self):
        return self.title
