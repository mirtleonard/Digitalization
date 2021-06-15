from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class UsernameValidator(UnicodeUsernameValidator):
    regex = r'^[\w.@+\- ]+$'

class User(AbstractUser):
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=40)
    activityReports = models.IntegerField(default=0)
    eventReports = models.IntegerField(default=0)
    birth = models.DateField(default='2002-04-02')
    validator = UsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators = [validator],
    )
    def __str__(self):
        return self.username
