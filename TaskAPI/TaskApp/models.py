from django.db import models
from datetime import datetime

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.task_name
