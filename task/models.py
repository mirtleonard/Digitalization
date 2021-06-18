from django.db import models
from user.models import User

# Create your models here.
class Task(models.Model):
    state = models.BooleanField(default=False)
    dueDate = models.DateTimeField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
