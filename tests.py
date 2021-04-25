from graph import Node, Conversation


start = Node("start")
place = Node("place")
date = Node("date")
time = Node("time")
end = Node("end")

start.add_question("Hello, how are you?")
start.next_node = place

place.add_question("Where do you want to eat your lunch?")
place.add_answer("Warsaw")
place.add_answer("Cracow")
place.add_answer("Poznan")
place.add_answer("Gdansk")
place.add_answer("Wroclaw")
place.next_node = date

date.add_question("When do you want to eat your lunch?")
date.answer_type = "date"
date.next_node = time

time.add_question("What time do you want to eat your lunch?")
time.answer_type = "time"
time.next_node = end

end.add_question("Ok, we note everything! Goodbye")

conv = Conversation(start=start)
# conv.add_edge(start, place)
# conv.add_edge(place, date)
# conv.add_edge(date, time)
# conv.add_edge(time, finish)


if __name__ == "__main__":
    conv.start_conversation()
