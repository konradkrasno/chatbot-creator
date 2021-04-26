from django.urls import path

from . import views

app_name = "chats"

urlpatterns = [
    path("", views.chat, name="chat"),
]
