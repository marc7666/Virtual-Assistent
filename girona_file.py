import colors
import urllib


def traffic_girona():
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
