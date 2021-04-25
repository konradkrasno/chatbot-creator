from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from nodes.models import Node


class NodeListView(ListView):
    model = Node
    template_name = "nodes/node/list.html"


class NodeDetailView(DetailView):
    model = Node
    template_name = "nodes/node/detail.html"


class CreateNodeView(CreateView):
    model = Node
    template_name = "nodes/node/form.html"
    fields = ["chat", "name", "answer_type"]
    success_url = reverse_lazy("nodes:node_list")


class UpdateNodeView(UpdateView):
    model = Node
    template_name = "nodes/node/form.html"
    fields = ["chat", "name", "nodes", "fail_node", "answer_type"]
    success_url = reverse_lazy("nodes:node_list")
