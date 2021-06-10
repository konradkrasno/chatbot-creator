from django.db import models
from django.urls import reverse

from account.models import User


class NotConfiguredError(Exception):
    pass


class Chat(models.Model):
    owner = models.ForeignKey(User, related_name="chats", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def get_start_node(self) -> "Node":
        for node in self.nodes.all():
            if node.name.lower() == "start":
                return node
        raise NotConfiguredError("The start node has not been created.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("nodes:node_list", args=[self.id])
