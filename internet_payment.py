"""
Internet payment information
"""
import urllib
import colors


def cat_int_pay():
    """
    This function prints the information to pay via internet
    :return:
    """
    print(colors.Color.BLUE + "Make the payment with digital certificate" + colors.Color.END)
    pay_and_certificate = urllib.parse.quote(
        'identitats.aoc.cat/o/oauth2/auth?response_type=code&client_id=tramits.'
        'transit.cat&redirect_uri=https'
        '://multestransit.gencat.cat/sctPagaments/AppJava/loginIdCat&scope='
        'autenticacio_usuari&access_type=online'
        '&approval_pompt=false&state=ca_ES')
    print('https://' + pay_and_certificate)
    print(colors.Color.BLUE + "Make the payment without digital certificate"
          + colors.Color.END)
    pay_without_certificate = urllib.parse.quote(
        'multestransit.gencat.cat/sctPagaments/AppJava/views/expedients/cerca.'
        'xhtml?set-locale=ca_ES')
    print('https://' + pay_without_certificate)
