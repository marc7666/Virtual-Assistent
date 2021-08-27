"""
Allegation of property rental file
"""
import urllib
import colors


def rental():
    """
     This function prints the link of the tax agency to pay the complaint
    """
    print(colors.Color.BLUE + "Allegation of property rental" + colors.Color.END)
    prop_rent = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/'
                                   'REGD-JDIT/FGDENAcceso?fTramite=ZZ065')
    print('https://' + prop_rent)
