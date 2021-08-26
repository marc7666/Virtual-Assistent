"""
Undeclared invoices and tickets complaint
"""
import urllib
import colors


def tickets():
    """
     This function prints the link of the tax agency to pay the complaint
    """
    print(colors.Color.BLUE + "Undeclared invoices and tickets complaint" + colors.Color.END)
    undeclared_comp = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/'
                                         'REGD-JDIT/FGDENAcceso?fTramite=ZZ062')
    print('https://' + undeclared_comp)
