"""
Chat bot main code
"""
# ****************************************
# Authorship:
# Jordi Planes Cid
# Marc Cervera Rosell
# Polytecnich school - University of Lleida
# ****************************************
import urllib.parse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import colors


# ******************* Auxiliar methods zone *******************

def print_instructions():
    """
    This method prints the instructions file
    """
    file = open('instructions.txt', 'r')
    content = file.read()
    print(colors.color.GREEN + content + colors.color.END)
    file.close()


def print_phone_information():
    """
    This method prints the 012 phone information.
    """
    file = open('012_information.txt', 'r')
    content = file.read()
    print(colors.color.GREEN + content + colors.color.END)
    file.close()


print(colors.color.YELLOW + "********** Loading all data **********" + colors.color.END)
CHATBOT = ChatBot('Virtual assistant')  # Creating a ChatBot
CHATBOT.storage.drop()  # Eliminates the dialog data
CONVERSATION = open('knowledge.bc', 'r').readlines()
TRAINER = ListTrainer(CHATBOT)  # This will train the CHATBOT object

TRAINER.train(CONVERSATION)  # Training the bot with the CONVERSATION list
print(colors.color.CYAN + "Welcome, I'm Charlie and I'm going to be your virtual assistant today."
      + colors.color.END)
print_instructions()
while True:  # Communication flow
    REQUEST = input('Me: ')  # Introduced by the user
    ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
    print('Charlie: ', ANSWER)
    if str(REQUEST) == "In person":  # Territorial links to pay the fee in person
        REQUEST = input('Me: ')  # Introduced by the user
        ANSWER = CHATBOT.get_response(REQUEST)  # Bot's answer
        print('Charlie: ', ANSWER)
        if str(REQUEST) == "Lleida":
            print(colors.color.BLUE + "Citizen attention office of Lleida link: "
                  + colors.color.END)
            LLEIDA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12443')
            print('http://' + LLEIDA_ATTENTION)
            print(colors.color.BLUE + "Territorial traffic service of Lleida link: "
                  + colors.color.END)
            LLEIDA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10293')
            print('http://' + LLEIDA_SERVICE)
        elif str(REQUEST) == "Barcelona":
            print(colors.color.BLUE + "Citizen attention office of Barcelona link: "
                  + colors.color.END)
            BARCELONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=6622')
            print('http://' + BARCELONA_ATTENTION)
            print(colors.color.BLUE + "Territorial traffic service of Barcelona link: "
                  + colors.color.END)
            BARCELONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10995')
            print('http://' + BARCELONA_SERVICE)
        elif str(REQUEST) == "Tarragona":
            print(colors.color.BLUE + "Citizen attention office of Tarragona link: "
                  + colors.color.END)
            TARRAGONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12444')
            print('http://' + TARRAGONA_ATTENTION)
            print(colors.color.BLUE + "Territorial traffic service of Tarragona link: "
                  + colors.color.END)
            TARRAGONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10996')
            print('http://' + TARRAGONA_SERVICE)
        elif str(REQUEST) == "Girona":
            print(colors.color.BLUE + "Citizen attention office of Girona link: "
                  + colors.color.END)
            GIRONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=17461')
            print('http://' + GIRONA_ATTENTION)
            print(colors.color.BLUE + "Territorial traffic service of Girona link: "
                  + colors.color.END)
            GIRONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=9715')
            print('http://' + GIRONA_SERVICE)
    if str(REQUEST) == "Phone":
        print(colors.color.BLUE + "Check the 012 opening hours:" + colors.color.END)
        OPENING_HOURS = urllib.parse.quote('web.gencat.cat/ca/contacte/012/')
        print('http://' + OPENING_HOURS)
        print_phone_information()
    if str(REQUEST) == "Via internet":
        print(colors.color.BLUE + "Make the payment with digital certificate" + colors.color.END)
        PAY_AND_CERTIFICATE = urllib.parse.quote(
            'identitats.aoc.cat/o/oauth2/auth?response_type=code&client_id=tramits.'
            'transit.cat&redirect_uri=https'
            '://multestransit.gencat.cat/sctPagaments/AppJava/loginIdCat&scope='
            'autenticacio_usuari&access_type=online'
            '&approval_pompt=false&state=ca_ES')
        print('https://' + PAY_AND_CERTIFICATE)
        print(colors.color.BLUE + "Make the payment without digital certificate"
              + colors.color.END)
        PAY_WITHOUT_CERTIFICATE = urllib.parse.quote(
            'multestransit.gencat.cat/sctPagaments/AppJava/views/expedients/cerca.'
            'xhtml?set-locale=ca_ES')
        print('https://' + PAY_WITHOUT_CERTIFICATE)
    if str(REQUEST) == "No":
        print(colors.color.BLUE + "Link of the 'Dirección general de tráfico' web to pay a fine"
              + colors.color.END)
        DGT = urllib.parse.quote('sede.DGT.gob.es/es/multas/paga-tu-multa/')
        print('https://' + DGT)
    if str(REQUEST) == "I want to present an allegation to a fine":
        print(
            colors.color.BLUE + "Link of the 'Dirección general de tráfico' web "
                                "to present an allegation"
            + colors.color.END)
        ALLEGATION_DGT = urllib.parse.quote(
            'sede.DGT.gob.es/es/multas/presenta-una-alegacion-o-recurso/')
        print('https://' + ALLEGATION_DGT)
    if str(ANSWER) == "See you the next time!":
        break
