from django.urls import path

from . import views

app_name = "nodes"

urlpatterns = [
    path("create/", views.CreateNodeView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateNodeView.as_view(), name="update"),
    path("list/<int:chat_id>", views.NodeListView.as_view(), name="node_list"),
    path("detail/<int:pk>/", views.NodeDetailView.as_view(), name="node_detail"),
    path(
        "question/add/<int:node_id>",
        views.AddQuestionView.as_view(),
        name="add_question",
    ),
    path("answer/add/<int:node_id>", views.AddAnswerView.as_view(), name="add_answer"),
]
