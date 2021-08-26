"""
Barcelona information file
"""
import urllib
import colors


def traffic_barcelona():
    """
    This function prints the links of Barcelona
    """
    print(colors.Color.BLUE + "Citizen attention office of Barcelona link: "
          + colors.Color.END)
    barcelona_attention = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=6622')
    print('http://' + barcelona_attention)
    print(colors.Color.BLUE + "Territorial traffic service of Barcelona link: "
          + colors.Color.END)
    barcelona_service = urllib.parse.quote(
        'sac.gencat.cat/sacgencat/AppJava/organisme_fitxa.jsp?codi=10995')
    print('http://' + barcelona_service)
