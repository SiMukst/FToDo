from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    taskname = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskname