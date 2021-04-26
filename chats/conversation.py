from random import choice
from typing import List, Dict, Tuple, Union

from chats.models import Chat
from nodes.models import Node


class Conversation:
    def __init__(self, chat_id: int, current_node_id: int = None):
        self._chat_id = chat_id
        if current_node_id:
            self.current_node = Node.objects.get(id=current_node_id)
        else:
            self.current_node = self.chat.get_start_node()
        self.checked_nodes: List = []
        self.user_answers: Dict = dict()

    @property
    def chat(self) -> "Chat":
        return Chat.objects.get(id=self._chat_id)

    def ask_question(self) -> str:
        return choice(self.current_node.questions.all()).question

    def parse_statement(self, statement: str) -> Tuple[str, Union["Node", None]]:
        # TODO finish
        nodes = self.current_node.rel_from_set.all()
        if nodes:
            return statement, choice(nodes).node_to
        return statement, None

    def save_answer(self, answer) -> None:
        self.user_answers[self.current_node] = answer

    def make_step(self, node: "Node") -> None:
        self.current_node = node

    def add_to_checked(self, node: "Node") -> None:
        self.checked_nodes.append(node)

    def get_response(self, statement: str) -> Dict:
        processed_statement, next_node = self.parse_statement(statement)
        question = self.ask_question()
        if next_node:
            self.save_answer(processed_statement)
            self.make_step(next_node)
        return {
            "chat_id": self._chat_id,
            "current_node_id": self.current_node.id,
            "question": question,
        }
