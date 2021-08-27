"""
Addresses and telephone numbers of the tax agency file
"""
import urllib
import colors


def tax_agency_info():
    """
     This function prints the link of the tax agency addresses and telephone numbers
    """
    print(colors.Color.BLUE + "Addresses and telephone numbers of the"
                              " tax agency" + colors.Color.END)
    agency_info = urllib.parse.quote('https://www.agenciatributaria.gob.es/AEAT.sede/ca_es/Inicio/'
                                     '_otros_/_Direcciones_y_telefonos_/_Direcciones_y'
                                     '_telefonos_.shtml')
    print('https://' + agency_info)
