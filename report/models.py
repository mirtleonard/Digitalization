from django.db import models

# Create your models here.


class Report(models.Model):
    username = models.CharField(max_length=240, default=" ")
    branch = models.CharField(max_length=240, default=" ")
    areas = models.CharField(max_length=240, default=" ")
    title = models.CharField(max_length=240, default=" ")
    location = models.CharField(max_length=240, default=" ")
    date = models.DateField()
    duration = models.CharField(max_length=240, default=" ")
    participants = models.CharField(max_length=240, default=" ")
    materials = models.CharField(max_length=240, default=" ")
    goals = models.TextField(max_length=240, default=" ")
    description = models.CharField(max_length = 5000)
    strengths = models.TextField()
    weaknesses = models.TextField()
    improvements = models.TextField()
    def __str__(self):
        return self.title
