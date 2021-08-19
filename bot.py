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
import subprocess


# ******************* Auxiliar methods zone *******************

def print_instructions():
    """
    This method prints the instructions file
    """
    file = open('instructions.txt', 'r')
    content = file.read()
    print(colors.Color.GREEN + content + colors.Color.END)
    file.close()


def print_phone_information():
    """
    This method prints the 012 phone information.
    """
    file = open('012_information.txt', 'r')
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
            print(colors.Color.BLUE + "Citizen attention office of Lleida link: "
                  + colors.Color.END)
            LLEIDA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12443')
            print('http://' + LLEIDA_ATTENTION)
            print(colors.Color.BLUE + "Territorial traffic service of Lleida link: "
                  + colors.Color.END)
            LLEIDA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10293')
            print('http://' + LLEIDA_SERVICE)
        elif str(REQUEST) == "Barcelona":
            print(colors.Color.BLUE + "Citizen attention office of Barcelona link: "
                  + colors.Color.END)
            BARCELONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=6622')
            print('http://' + BARCELONA_ATTENTION)
            print(colors.Color.BLUE + "Territorial traffic service of Barcelona link: "
                  + colors.Color.END)
            BARCELONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10995')
            print('http://' + BARCELONA_SERVICE)
        elif str(REQUEST) == "Tarragona":
            print(colors.Color.BLUE + "Citizen attention office of Tarragona link: "
                  + colors.Color.END)
            TARRAGONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12444')
            print('http://' + TARRAGONA_ATTENTION)
            print(colors.Color.BLUE + "Territorial traffic service of Tarragona link: "
                  + colors.Color.END)
            TARRAGONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10996')
            print('http://' + TARRAGONA_SERVICE)
        elif str(REQUEST) == "Girona":
            print(colors.Color.BLUE + "Citizen attention office of Girona link: "
                  + colors.Color.END)
            GIRONA_ATTENTION = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=17461')
            print('http://' + GIRONA_ATTENTION)
            print(colors.Color.BLUE + "Territorial traffic service of Girona link: "
                  + colors.Color.END)
            GIRONA_SERVICE = urllib.parse.quote(
                'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=9715')
            print('http://' + GIRONA_SERVICE)
    if str(REQUEST) == "Phone":  # This way is only available in Catalonia
        print(colors.Color.BLUE + "Check the 012 opening hours:" + colors.Color.END)
        OPENING_HOURS = urllib.parse.quote('web.gencat.cat/ca/contacte/012/')
        print('http://' + OPENING_HOURS)
        print_phone_information()
    if str(REQUEST) == "Via internet":  # This way is for persons who live in Catalonia
        print(colors.Color.BLUE + "Make the payment with digital certificate" + colors.Color.END)
        PAY_AND_CERTIFICATE = urllib.parse.quote(
            'identitats.aoc.cat/o/oauth2/auth?response_type=code&client_id=tramits.'
            'transit.cat&redirect_uri=https'
            '://multestransit.gencat.cat/sctPagaments/AppJava/loginIdCat&scope='
            'autenticacio_usuari&access_type=online'
            '&approval_pompt=false&state=ca_ES')
        print('https://' + PAY_AND_CERTIFICATE)
        print(colors.Color.BLUE + "Make the payment without digital certificate"
              + colors.Color.END)
        PAY_WITHOUT_CERTIFICATE = urllib.parse.quote(
            'multestransit.gencat.cat/sctPagaments/AppJava/views/expedients/cerca.'
            'xhtml?set-locale=ca_ES')
        print('https://' + PAY_WITHOUT_CERTIFICATE)
    if str(REQUEST) == "No":  # Persons who not live in Catalonia
        print(colors.Color.BLUE + "Link of the 'Dirección general de tráfico' web to pay a fine"
              + colors.Color.END)
        DGT = urllib.parse.quote('sede.DGT.gob.es/es/multas/paga-tu-multa/')
        print('https://' + DGT)
    if str(REQUEST) == "I want to present an allegation to a fine":
        print(
            colors.Color.BLUE + "Link of the 'Dirección general de tráfico' web "
                                "to present an allegation"
            + colors.Color.END)
        ALLEGATION_DGT = urllib.parse.quote(
            'sede.DGT.gob.es/es/multas/presenta-una-alegacion-o-recurso/')
        print('https://' + ALLEGATION_DGT)
    if str(REQUEST) == "Town hall taxes and fines":  # The link of the town hall can be changed
        print(colors.Color.BLUE + "Link of the tributary service of Lleida town hall"
              + colors.Color.END)
        TOWN_HALL = urllib.parse.quote('ajuntamentlleida.tributoslocales.es'
                                       '/ovt/EXPE/251203/ALLEIDA/noauth/cobro')
        print('https://' + TOWN_HALL)
    if str(REQUEST) == "I want to go sightseeing":
        print(colors.Color.BLUE + "Link to the Lleida tourist office" + colors.Color.END)
        TOURISM_OFFICE = urllib.parse.quote('www.turismedelleida.cat/')
        print('https://' + TOURISM_OFFICE)
        print(colors.Color.YELLOW + "Most important places of Lleida" + colors.Color.END)
        subprocess.call('./print_pictures.sh')
    if str(ANSWER) == "See you the next time!":
        break
