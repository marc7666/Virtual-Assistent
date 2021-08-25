import colors
import urllib


def traffic_lleida():
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
