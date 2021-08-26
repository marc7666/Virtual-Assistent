"""
dgt fine payment file
"""
import urllib
import colors


def traffic_dgt():
    """
    This function prints the dgt link to pay a fine
    """
    print(colors.Color.BLUE + "Link of the 'Dirección general de tráfico' web to pay a fine"
          + colors.Color.END)
    dgt = urllib.parse.quote('sede.dgt.gob.es/es/multas/paga-tu-multa/')
    print('https://' + dgt)
