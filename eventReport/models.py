from django.db import models
from datetime import date
# Create your models here.

class EventReport(models.Model):
    username = models.CharField(max_length=240)
    center = models.CharField(max_length= 100)
    eventType = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    members = models.CharField(max_length = 1000)
    location = models.CharField(max_length = 240)
    description = models.TextField()
    beginingDate = models.DateTimeField(blank = True, null = True)
    endDate = models.DateTimeField(blank = True, null = True)
    def __str__(self):
        return self.title
