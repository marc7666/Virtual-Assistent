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
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import address_and_tels
import barcelona_file
import cash_payments
import colors
import complaint_ord
import dgt_allegation
import dgt_fine
import e_commerce
import girona_file
import internet_payment
import lleida_file
import phone_payment
import property_rental
import sightseeing
import software_complaint
import tarragona_file
import town_hall
import undeclared_tickets


# ******************* Auxiliary methods zone *******************


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
    if str(REQUEST) == "Tributary complaint":
        COMPLAINT_TYPES = ["Ordinary complaint", "Reporting undeclared invoices and receipts",
                           "Allegation of sales suppression software",
                           "Allegation of e-commerce and online fraud",
                           "Allegation of property rental", "Reporting cash payments"]

        for index, type_c in enumerate(COMPLAINT_TYPES):
            print(colors.Color.CYAN + type_c + colors.Color.END)
        REQUEST = input('Me: ')  # Introduced by the user
        ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
        print('Charlie: ', ANSWER)
        if str(REQUEST) == "Ordinary":
            complaint_ord.ordinary()
        elif str(REQUEST) == "Reporting undeclared invoices and receipts":
            undeclared_tickets.tickets()
        elif str(REQUEST) == "Allegation of sales suppression software":
            software_complaint.software_sales()
        elif str(REQUEST) == "Allegation of e-commerce and online fraud":
            e_commerce.web_fraud()
        elif str(REQUEST) == "Allegation of property rental":
            property_rental.rental()
        elif str(REQUEST) == "Reporting cash payments":
            cash_payments.cash()
    if str(REQUEST) == "Addresses and telephone numbers of the tax agency":
        address_and_tels.tax_agency_info()
    if str(ANSWER) == "See you the next time!":
        sys.exit()
