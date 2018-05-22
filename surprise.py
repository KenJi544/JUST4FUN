#!/usr/bin/python

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("FU")

conversation = [" sal ba pl",
        "bai esti prost!",
        "ma-ta-i curva",
        "Apostol pidar",
        "sugi pl"]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

if __name__ == "__main__":
    while True:
        try:
            user_input = raw_input()
            response = chatbot.get_response(user_input)
            print(response)
        except(EOFError, KeyboardInterrupt, SystemExit):
            break
