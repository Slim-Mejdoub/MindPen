from django.db import models
from Endeavors.models import Endeavor


class Task(models.Model):
    endeavor_id = models.ForeignKey(Endeavor, on_delete=models.CASCADE, null=True, related_name="todo_tasks")
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    starting_time = models.DateTimeField()
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title
