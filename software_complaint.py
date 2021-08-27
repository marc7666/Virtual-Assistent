"""
Allegation of sales suppression software file
"""
import urllib
import colors


def software_sales():
    """
     This function prints the link of the tax agency to pay the complaint
    """
    print(colors.Color.BLUE + "Allegation of sales suppression software" + colors.Color.END)
    software_comp = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/'
                                       'REGD-JDIT/FGDENAcceso?fTramite=ZZ063')
    print('https://' + software_comp)
