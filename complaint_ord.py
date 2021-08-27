"""
Ordinary complaint file
"""
import urllib
import colors


def ordinary():
    """
    This function prints the link of the tax agency to pay an ordinary complaint
    """
    print(colors.Color.BLUE + "To pay an ordinary complaint" + colors.Color.END)
    ordinary_comp = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/REGD-JDIT/'
                                       'FGDENAcceso?fTramite=ZZ061')
    print('https://' + ordinary_comp)
