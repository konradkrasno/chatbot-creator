from django.urls import path

from . import views

app_name = "nodes"

urlpatterns = [
    path("create/", views.CreateNodeView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateNodeView.as_view(), name="update"),
    path("list/", views.NodeListView.as_view(), name="node_list"),
    path("detail/<int:pk>/", views.NodeDetailView.as_view(), name="node_detail"),
]
