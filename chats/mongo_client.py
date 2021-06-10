from pymongo import MongoClient
from datetime import datetime

client = MongoClient(host="mongo", port=27017)
chat_db = client.chat
user_answers = chat_db.user_answers


class UserAnswer(object):
    def __init__(self, user_id: int, chat_id: int):
        self.user_id = user_id
        self.chat_id = chat_id

    def save_answer(self, question_id: int, question: str, answer: str):
        item = {
            "user_id": self.user_id,
            "chat_id": self.chat_id,
            "question_id": question_id,
            "question": question,
            "answer": answer,
            "answer_time": datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
        }
        user_answers.insert_one(item)
