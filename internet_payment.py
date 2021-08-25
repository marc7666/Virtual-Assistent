import colors
import urllib


def cat_int_pay():
    print(colors.Color.BLUE + "Make the payment with digital certificate" + colors.Color.END)
    PAY_AND_CERTIFICATE = urllib.parse.quote(
        'identitats.aoc.cat/o/oauth2/auth?response_type=code&client_id=tramits.'
        'transit.cat&redirect_uri=https'
        '://multestransit.gencat.cat/sctPagaments/AppJava/loginIdCat&scope='
        'autenticacio_usuari&access_type=online'
        '&approval_pompt=false&state=ca_ES')
    print('https://' + PAY_AND_CERTIFICATE)
    print(colors.Color.BLUE + "Make the payment without digital certificate"
          + colors.Color.END)
    PAY_WITHOUT_CERTIFICATE = urllib.parse.quote(
        'multestransit.gencat.cat/sctPagaments/AppJava/views/expedients/cerca.'
        'xhtml?set-locale=ca_ES')
    print('https://' + PAY_WITHOUT_CERTIFICATE)
