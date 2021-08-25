import colors
import urllib


def traffic_tarragona():
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
