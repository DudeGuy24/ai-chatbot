from chatterbot import ChatBot

chatbot = ChatBot("Crackbot")

exit_conditions = (":q", "quit", "bye")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"CRACKBOT:  {chatbot.get_response(query)}")