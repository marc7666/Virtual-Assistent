"""
Chat bot main code
"""
# ****************************************
# Authorship:
# Jordi Planes Cid
# Marc Cervera Rosell
# Polytecnich school - University of Lleida
# ****************************************
import sys
import urllib.parse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import barcelona_file
import colors

# ******************* Auxiliary methods zone *******************
import dgt_allegation
import dgt_fine
import girona_file
import internet_payment
import lleida_file
import phone_payment
import sightseeing
import tarragona_file
import town_hall


def print_instructions():
    """
    This method prints the instructions file
    """
    file = open('instructions.txt', 'r')
    content = file.read()
    print(colors.Color.GREEN + content + colors.Color.END)
    file.close()


print(colors.Color.YELLOW + "********** Loading all data **********" + colors.Color.END)
CHATBOT = ChatBot('Virtual assistant')  # Creating a ChatBot
CHATBOT.storage.drop()  # Eliminates the dialog data
CONVERSATION = open('knowledge.bc', 'r').readlines()
TRAINER = ListTrainer(CHATBOT)  # This will train the CHATBOT object

TRAINER.train(CONVERSATION)  # Training the bot with the CONVERSATION list
print_instructions()
print(colors.Color.CYAN + "Welcome, I'm Charlie and I'm going to be your virtual assistant today."
      + colors.Color.END)
print(colors.Color.PURPLE + "REMEMBER THAT THIS IS NOT AN IGNORE CASE PROGRAM!! "
                            "WRITE THE COMMANDS AS IN THE USER MANUAL ARE" + colors.Color.END)
print(colors.Color.PURPLE + "IMPORTANT!!!! THE DEFAULT LANGUAGE FOR THE PAGES IS CATALAN"
      + colors.Color.END)
while True:  # Communication flow
    REQUEST = input('Me: ')  # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
    print('Charlie: ', ANSWER)
    if str(REQUEST) == "In person":  # Territorial links to pay the fee in person
        REQUEST = input('Me: ')  # Introduced by the user
        ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
        print('Charlie: ', ANSWER)
        if str(REQUEST) == "Lleida":
            lleida_file.traffic_lleida()
        elif str(REQUEST) == "Barcelona":
            barcelona_file.traffic_barcelona()
        elif str(REQUEST) == "Tarragona":
            tarragona_file.traffic_tarragona()
        elif str(REQUEST) == "Girona":
            girona_file.traffic_girona()
    if str(REQUEST) == "Phone":  # This way is only available in Catalonia
        phone_payment.cat_012()
    if str(REQUEST) == "Via internet":  # This way is for persons who live in Catalonia
        internet_payment.cat_int_pay()
    if str(REQUEST) == "No":  # Persons who not live in Catalonia
        dgt_fine.traffic_dgt()
    if str(REQUEST) == "I want to present an allegation to a fine":
        dgt_allegation.allegation()
    if str(REQUEST) == "Town hall taxes and fines":  # The link of the town hall can be changed
        town_hall.taxes_and_fines()
    if str(REQUEST) == "I want to go sightseeing":
        sightseeing.sightseeing_lleida()
    if str(ANSWER) == "See you the next time!":
        sys.exit()
