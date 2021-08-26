"""
Lleida information file
"""
import urllib
import colors


def traffic_lleida():
    """
    This function prints the links of Lleida
    """
    print(colors.Color.BLUE + "Citizen attention office of Lleida link: "
          + colors.Color.END)
    lleida_attention = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=12443')
    print('http://' + lleida_attention)
    print(colors.Color.BLUE + "Territorial traffic service of Lleida link: "
          + colors.Color.END)
    lleida_service = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10293')
    print('http://' + lleida_service)
