from typing import Set, List, Dict
from collections import defaultdict
from random import choice


class Node:
    def __init__(self, name):
        # self.name = name
        # self.previous_node: "Node" = self
        # self.next_node: "Node" = None
        # self.questions: List = []
        # self.answers: List = []
        # self.answer_type: str
        self.checked: bool = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Node: {self.name}>"

    # def add_question(self, question: str) -> None:
    #     self.questions.append(question)
    #
    # def delete_question(self, question: str) -> None:
    #     self.questions.remove(question)
    #
    # def add_answer(self, answer: str) -> None:
    #     self.answers.append(answer)
    #
    # def delete_answer(self, answer: str) -> None:
    #     self.answers.remove(answer)


# class Graph:
#     def __init__(self, start: Node, end: Node):
#         self._start: Node = start
#         self._end: Node = end
#         self.current_node: Node = self._start
#         self.graph = defaultdict(set)
#         self.checked_nodes: List = []
#
#     def add_edge(self, u: Node, v: Node) -> None:
#         self.graph[u].add(v)
#
#     def get_successors(self) -> Set:
#         return self.graph.get(self.current_node)
#


class Printer:
    def draw_graph(self):
        pass


class Conversation:
    def __init__(self, start: Node):
        self._start: Node = start
        # self._nodes: List = nodes
        self.current_node: Node = self._start
        # self.graph = defaultdict(set)
        self.checked_nodes: List = []
        self.user_answers: Dict = dict()

    def ask_question(self) -> str:
        return choice(self.current_node.questions)

    def parse_answer(self, answer) -> str:
        return answer

    def save_answer(self, answer) -> None:
        self.user_answers[self.current_node] = answer

    @staticmethod
    def get_answer() -> str:
        answer = input(">> ")
        return answer

    def make_step(self, node: Node) -> None:
        self.current_node = node

    def add_to_checked(self, node: Node) -> None:
        self.checked_nodes.append(node)

    def start_conversation(self) -> None:
        while True:
            print(self.ask_question())
            if self.current_node.next_node is None:
                return
            answer = self.get_answer()
            processed_answer = self.parse_answer(answer)
            if processed_answer:
                self.save_answer(processed_answer)
                self.make_step(self.current_node.next_node)
            else:
                self.make_step(self.current_node.previous_node)


class ChatCreator:
    def create_node(self, name: str) -> Node:
        return Node(name=name)

    def add_node(self):
        pass
