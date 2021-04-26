from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from chats.conversation import Conversation


@api_view(["POST"])
@parser_classes([JSONParser])
def chat(request, format=None):
    # data = request.data.get("data")
    data = {
        "chat_id": 1,
        "current_node_id": None,
        "statement": "Hello world",
    }
    conv = Conversation(
        chat_id=data.get("chat_id"), current_node_id=data.get("current_node_id")
    )
    result = conv.get_response(data.get("statement"))
    return Response(result)
