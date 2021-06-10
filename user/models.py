from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=40)
    reports = models.IntegerField(default=0)
    birth = models.DateField()
    def __str__(self):
        return self.username
