"""
Reporting cash payments file
"""
import urllib
import colors


def cash():
    """
     This function prints the link of the tax agency to pay the complaint
    """
    print(colors.Color.BLUE + "Allegation of property rental" + colors.Color.END)
    cash_p = urllib.parse.quote('www2.agenciatributaria.gob.es/wlpl/BUCV-JDIT/'
                                'AutenticaDniNieContrasteh?ref=%2Fwlpl%2FOVCT%2DCXEW%2F'
                                'SelectorAcceso%3Fref%3D%252Fwlpl%252FREGD%2DJDIT%252FF'
                                'GDEN%253FfTramite%253DZZ131%26aut%3DCPR')
    print('https://' + cash_p)
