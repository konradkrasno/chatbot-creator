from django import forms

from nodes.models import Node


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ("chat", "name", "answer_type")
