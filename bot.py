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
from chatterbot.trainers import ChatterBotCorpusTrainer
# ChatterBotCorpusTrainer => It already contains basic information of a ChatBot,
# so we can have a conversation with our ChatBot

CHATBOT = ChatBot('Virtual assistent') # Creating a ChatBot

TRAINER = ChatterBotCorpusTrainer(CHATBOT) # This will train the CHATBOT object

TRAINER.train('chatterbot.corpus.english') # Training the bot in english

while True: # Communication flow
    REQUEST = input('Me: ') # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST) # Bot's answer
    print('Virtual assistent: ', ANSWER)
