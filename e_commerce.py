"""
Allegation of e-commerce and online fraud file
"""
import urllib
import colors


def web_fraud():
    """
     This function prints the link of the tax agency to pay the complaint
    """
    print(colors.Color.BLUE + "Allegation of e-commerce and online fraud" + colors.Color.END)
    commerce_fraud = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/'
                                        'REGD-JDIT/FGDENAcceso?fTramite=ZZ064')
    print('https://' + commerce_fraud)
