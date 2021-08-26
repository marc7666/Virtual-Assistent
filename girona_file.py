"""
Girona information file
"""
import urllib
import colors


def traffic_girona():
    """
    This function prints the links of Girona
    """
    print(colors.Color.BLUE + "Citizen attention office of Girona link: "
          + colors.Color.END)
    girona_attention = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=17461')
    print('http://' + girona_attention)
    print(colors.Color.BLUE + "Territorial traffic service of Girona link: "
          + colors.Color.END)
    girona_service = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=9715')
    print('http://' + girona_service)
