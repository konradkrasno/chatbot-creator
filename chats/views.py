from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from chats.conversation import Conversation


@api_view(["POST"])
@parser_classes([JSONParser])
def chat(request, format=None):
    conv = Conversation(
        user_id=request.user.id,
        chat_id=request.data.get("chat_id"),
        current_node_id=request.data.get("current_node_id"),
        prev_qstn_id=request.data.get("question_id"),
    )
    result = conv.get_response(request.data.get("statement"))
    return Response(result)
