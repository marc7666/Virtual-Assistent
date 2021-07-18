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
import urlib.parse
import colors
print(colors.color.YELLOW + "********** Loading all data **********" + colors.color.END)
CHATBOT = ChatBot('Virtual assistant') # Creating a ChatBot
CHATBOT.storage.drop() # Eliminates the dialog data
CONVERSATION = open('knowledge.bc', 'r').readlines()
TRAINER = ListTrainer(CHATBOT) # This will train the CHATBOT object

TRAINER.train(CONVERSATION) # Training the bot with the CONVERSATION list
print(colors.color.CYAN + "Welcome, I'm Charlie and I'm going to be your virtual assitent today." + colors.color.END)
while True: # Communication flow
    REQUEST = input('Me: ') # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST) # Bot's answer
    print('Charlie: ', ANSWER)
    if str(ANSWER).startswith("See"): # Finish condition
        break
    if str(REUQEST) == "DGT":
        print(colors.color.BLUE + "Acces to the following link: " + colors.color.END)
        institution = urlib.parse.quote('sede.dgt.gob.es/es/multas/#')
        print("https://" + institution)
