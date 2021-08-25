import bot
import colors
import urllib


def fines():
    if str(bot.REQUEST) == "In person":  # Territorial links to pay the fee in person
        REQUEST = input('Me: ')  # Introduced by the user
        ANSWER = bot.CHATBOT.get_response(REQUEST)  # Bot's answer
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
        bot.print_phone_information()
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
