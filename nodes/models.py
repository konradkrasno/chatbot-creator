from django.db import models
from django.urls import reverse

from chats.models import Chat


class AnswerType(models.TextChoices):
    GENERAL = "general"
    DATE = "date"
    TIME = "time"


class Node(models.Model):
    chat = models.ForeignKey(Chat, related_name="nodes", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    answer_type = models.CharField(max_length=50, choices=AnswerType.choices)
    nodes = models.ManyToManyField(
        "self", through="Answer", related_name="success_predecessors", symmetrical=False
    )
    fail_node = models.OneToOneField(
        "Node",
        related_name="fail_predecessor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.chat.name}:{self.name}"

    def get_absolute_url(self):
        return reverse("nodes:node_detail", args=[self.id])


class Question(models.Model):
    question = models.CharField(max_length=200)
    node = models.ForeignKey(Node, related_name="questions", on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.CharField(max_length=200, blank=True)
    node_from = models.ForeignKey(
        Node, related_name="rel_from_set", on_delete=models.CASCADE
    )
    node_to = models.ForeignKey(
        Node, related_name="rel_to_set", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"chat:{self.node_from.chat.name};"
            f" from node:{self.node_from.name}; to node:{self.node_to.name};"
            f" answer: {self.answer}"
        )
