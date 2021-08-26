"""
dgt fine allegation file
"""
import urllib
import colors


def allegation():
    """
    This function prints the DGT link to present an allegation to a fine
    """
    print(
        colors.Color.BLUE + "Link of the 'Dirección general de tráfico' web "
                            "to present an allegation"
        + colors.Color.END)
    allegation_dgt = urllib.parse.quote(
        'sede.dgt.gob.es/es/multas/presenta-una-alegacion-o-recurso/')
    print('https://' + allegation_dgt)
