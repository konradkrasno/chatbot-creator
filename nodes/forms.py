from django import forms

from nodes.models import Node


class UpdateNodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ("chat", "name", "fail_node", "answer_type")
