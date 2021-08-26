"""
Tarragona information file
"""
import urllib
import colors


def traffic_tarragona():
    """
    This function prints the links of Tarragona
    """
    print(colors.Color.BLUE + "Citizen attention office of Tarragona link: "
          + colors.Color.END)
    tarragona_attention = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12444')
    print('http://' + tarragona_attention)
    print(colors.Color.BLUE + "Territorial traffic service of Tarragona link: "
          + colors.Color.END)
    tarragona_service = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10996')
    print('http://' + tarragona_service)
