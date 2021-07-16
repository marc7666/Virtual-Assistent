'''
Chat bot main code
'''
# ****************************************
# Authorship:
# Jordi Planes Cid
# Marc Cervera Rosell
# Polytecnich school - University of Lleida
# ****************************************
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import string

CHATBOT = ChatBot('Virtual assistant') # Creating a ChatBot
CHATBOT.storage.drop() # Eliminates the dialog data
CONVERSATION = open('knowledge.bc', 'r').readlines()
TRAINER = ListTrainer(CHATBOT) # This will train the CHATBOT object

TRAINER.train(CONVERSATION) # Training the bot with the CONVERSATION list
while True: # Communication flow
    REQUEST = input('Me: ') # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST) # Bot's answer
    print('Virtual assistant: ', ANSWER)
    if str(ANSWER).startswith("See"): # Finish condition
        break
