from django.db import models
from user.models import User

# Create your models here.
class Task(models.Model):
    dueDate = models.DateTimeField()
    title = models.CharField(max_length=100)
    state = models.BooleanField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
