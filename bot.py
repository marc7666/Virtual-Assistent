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
import urllib.parse
import string
import colors


# ******************* Auxiliar methods zone *******************

def print_instructions():
    file = open('instructions.txt', 'r')
    content = file.read()
    print(colors.color.GREEN + content + colors.color.END)
    file.close()


print(colors.color.YELLOW + "********** Loading all data **********" + colors.color.END)
CHATBOT = ChatBot('Virtual assistant')  # Creating a ChatBot
CHATBOT.storage.drop()  # Eliminates the dialog data
CONVERSATION = open('knowledge.bc', 'r').readlines()
TRAINER = ListTrainer(CHATBOT)  # This will train the CHATBOT object

TRAINER.train(CONVERSATION)  # Training the bot with the CONVERSATION list
print(colors.color.CYAN + "Welcome, I'm Charlie and I'm going to be your virtual assistant today." + colors.color.END)
print_instructions()
while True:  # Communication flow
    REQUEST = input('Me: ')  # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
    print('Charlie: ', ANSWER)
    if str(REQUEST) == "Presentially":
        REQUEST = input('Me: ')  # Introduced by the user
        ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
        print('Charlie: ', ANSWER)
        if str(REQUEST) == "Lleida":
            print('Links of Lleida: ')
            print(colors.color.BLUE + "Citizen attention office of Lleida link: " + colors.color.END)
            lleida_attention = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12443')
            print('http://' + lleida_attention)
            print(colors.color.BLUE + "Territorial traffic service of Lleida link: " + colors.color.END)
            lleida_service = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10293')
            print('http://' + lleida_service)
        elif str(REQUEST) == "Barcelona":
            print('Links of Barcelona: ')
            print(colors.color.BLUE + "Citizen attention office of Barcelona link: " + colors.color.END)
            barcelona_attention = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=6622')
            print('http://' + barcelona_attention)
            print(colors.color.BLUE + "Territorial traffic service of Barcelona link: " + colors.color.END)
            barcelona_service = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10995')
            print('http://' + barcelona_service)
        elif str(REQUEST) == "Tarragona":
            print('Links of Tarragona: ')
            print(colors.color.BLUE + "Citizen attention office of Tarragona link: " + colors.color.END)
            tarragona_attention = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12444')
            print('http://' + tarragona_attention)
            print(colors.color.BLUE + "Territorial traffic service of Tarragona link: " + colors.color.END)
            tarragona_service = urllib.parse.quote('sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10996')
            print('http://' + tarragona_service)
