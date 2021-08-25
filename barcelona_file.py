import colors
import urllib


def traffic_barcelona():
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
