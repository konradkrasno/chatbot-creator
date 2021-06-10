from chats.models import Chat
from django.http import HttpResponseForbidden


class GetChatMixin(object):
    chat_object = None

    def get_chat_object(self):
        chat_id = self.get_form_kwargs()["data"].get("chat")
        return Chat.objects.get(id=chat_id)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.chat_object = self.get_chat_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return self.chat_object.get_absolute_url()
