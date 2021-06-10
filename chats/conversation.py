from random import choice
from typing import List, Dict, Tuple, Union

from chats.models import Chat
from nodes.models import Node, Question
from chats.mongo_client import UserAnswer


class Conversation:
    def __init__(
        self,
        user_id: int,
        chat_id: int,
        current_node_id: int = None,
        prev_qstn_id: int = None,
    ):
        self.user_id: int = user_id
        self._chat_id = chat_id

        if current_node_id:
            self.current_node = Node.objects.get(id=current_node_id)
        else:
            self.current_node = self.chat.get_start_node()

        try:
            self.prev_question: Question = Question.objects.get(id=prev_qstn_id)
        except Question.DoesNotExist:
            self.prev_question: Question = Question()

        self.checked_nodes: List = []
        self.user_answers: UserAnswer = UserAnswer(user_id, chat_id)

    @property
    def chat(self) -> "Chat":
        return Chat.objects.get(id=self._chat_id)

    def ask_question(self) -> Question:
        return choice(self.current_node.questions.all())

    def parse_statement(self, statement: str) -> Tuple[str, Union["Node", None]]:
        # TODO finish
        nodes = self.current_node.rel_from_set.all()
        if nodes:
            return statement, choice(nodes).node_to
        return statement, None

    def save_answer(self, question: Question, answer: str) -> None:
        self.user_answers.save_answer(question.id, question.question, answer)

    def make_step(self, node: "Node") -> None:
        self.current_node = node

    def add_to_checked(self, node: "Node") -> None:
        self.checked_nodes.append(node)

    def get_response(self, statement: str) -> Dict:
        processed_statement, next_node = self.parse_statement(statement)
        question = self.ask_question()
        if next_node:
            self.save_answer(self.prev_question, processed_statement)
            self.make_step(next_node)
        return {
            "chat_id": self._chat_id,
            "current_node_id": self.current_node.id,
            "prev_question_id": self.prev_question.id,
            "question": question.question,
            "question_id": question.id,
        }
