from django.db import models

# Create your models here.


class Report(models.Model):
    username = models.CharField(max_length=40);
    areas = models.CharField(max_length=40);
    location = models.CharField(max_length=40);
    title = models.CharField(max_length=40);
    duration = models.CharField(max_length=40);
    date = models.DateField();
    participants = models.CharField(max_length=40);
    description = models.CharField(max_length=40);
    goals = models.CharField(max_length=40);
    strengths = models.CharField(max_length=40);
    weaknesses = models.CharField(max_length=40);
    improvements = models.CharField(max_length=40);
    branch = models.CharField(max_length=40)
    def __str__(self):
        return self.title
