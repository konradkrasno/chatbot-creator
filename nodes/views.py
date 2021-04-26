from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from nodes.models import Node, Question, Answer
from nodes.forms import UpdateNodeForm


class NodeListView(ListView):
    model = Node
    template_name = "nodes/node/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(chat_id=self.kwargs.get("chat_id"))


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
    form_class = UpdateNodeForm

    def get_success_url(self):
        return self.object.get_absolute_url()


class AddQuestionView(CreateView):
    model = Question
    template_name = "nodes/node/form.html"
    fields = ["question"]

    def form_valid(self, form):
        question = form.save(commit=False)
        question.node_id = self.kwargs.get("node_id")
        question.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("nodes:node_detail", args=[self.kwargs.get("node_id")])


class AddAnswerView(CreateView):
    model = Answer
    template_name = "nodes/node/form.html"
    fields = ["answer", "node_to"]

    def form_valid(self, form):
        question = form.save(commit=False)
        question.node_from_id = self.kwargs.get("node_id")
        question.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("nodes:node_detail", args=[self.kwargs.get("node_id")])
