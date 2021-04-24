from typing import Set, List, Dict
from collections import defaultdict


class Node:
    questions: List = []
    answers: List = []
    checked: bool = False

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def add_question(self, question: str) -> None:
        self.questions.append(question)

    def delete_question(self, question: str) -> None:
        self.questions.remove(question)

    def add_answer(self, answer: str) -> None:
        self.answers.append(answer)

    def delete_answer(self, answer: str) -> None:
        self.answers.remove(answer)


class Graph:
    graph = defaultdict(set)
    checked_nodes: List = []

    def __init__(self, start: Node):
        self._start: Node = start
        self.current_node: Node = self._start

    def add_edge(self, u: Node, v: Node) -> None:
        self.graph[u].add(v)

    def get_successors(self) -> Set:
        return self.graph.get(self.current_node)

    def make_step(self, node: Node) -> None:
        if node in self.get_successors():
            self.current_node = node

    def add_to_checked(self, node: Node) -> None:
        self.checked_nodes.append(node)


class Printer(Graph):
    def draw_graph(self):
        pass


class Conversation(Graph):
    user_answers: Dict = dict()

    def ask_question(self):
        pass

    def parse_answer(self, answer) -> str:
        pass

    def save_answer(self, node, answer) -> None:
        self.user_answers[node] = answer


class ChatCreator(Graph):
    def create_node(self, name: str) -> Node:
        return Node(name=name)

    def add_node(self):
        pass
