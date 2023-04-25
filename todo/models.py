from django.db import models
from users.models import User


class Todo(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='my_todo')
    title = models.CharField(max_length=20)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completion_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
