from django.db import models

# Create your models here.

class EventReport(models.Model):
    username = models.CharField(max_length=240)
    center = models.CharField(max_length= 100)
    eventType = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    members = models.CharField(max_length = 1000)
    description = models.TextField(max_length = 10000)
    location = models.CharField(max_length=240)
    beginingDate = models.DateTimeField()
    endDate = models.DateTimeField()
    def __str__(self):
        return self.title
