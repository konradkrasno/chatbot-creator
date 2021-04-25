from django.db import models
from account.models import User


class Chat(models.Model):
    owner = models.ForeignKey(User, related_name="chats", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
