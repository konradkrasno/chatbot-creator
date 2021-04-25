from django.db import models
from chats.models import Chat


class AnswerType(models.TextChoices):
    GENERAL = "general"
    DATE = "date"
    TIME = "time"


class Node(models.Model):
    chat = models.ForeignKey(Chat, related_name="nodes", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    nodes = models.ManyToManyField("self", related_name="success_predecessor")
    fail_node = models.OneToOneField(
        "Node",
        related_name="fail_predecessor",
        on_delete=models.SET_NULL,
        null=True,
    )
    answer_type = models.CharField(max_length=50, choices=AnswerType.choices)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=200)
    node = models.ForeignKey(Node, related_name="questions", on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=200)
    node = models.ForeignKey(Node, related_name="answers", on_delete=models.CASCADE)
