from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer 

chatbot = ChatBot("Crackbot")

trainer = ListTrainer(chatbot)
trainer.train ([
    "Hello",
    "Whatchu want?"
])
trainer.train ([
    "What's your name?",
    "Name's Crackbot, what can I do ya for?"
])

exit_conditions = (":q", "quit", "bye")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"CRACKBOT:  {chatbot.get_response(query)}")