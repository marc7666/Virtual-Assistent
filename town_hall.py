"""
Town hall taxes and fines file
"""
import urllib
import colors


def taxes_and_fines():
    """
    This function will print the tributary service of Lleida (in this case) town hall
    """
    print(colors.Color.BLUE + "Link of the tributary service of Lleida town hall"
          + colors.Color.END)
    town_hall = urllib.parse.quote('ajuntamentlleida.tributoslocales.es'
                                   '/ovt/EXPE/251203/ALLEIDA/noauth/cobro')
    print('https://' + town_hall)
