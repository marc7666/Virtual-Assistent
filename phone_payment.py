import colors
import urllib


def print_phone_information():
    """
    This method prints the 012 phone information.
    """
    file = open('012_information.txt', 'r')
    content = file.read()
    print(colors.Color.GREEN + content + colors.Color.END)
    file.close()


def cat_012():
    print(colors.Color.BLUE + "Check the 012 opening hours:" + colors.Color.END)
    OPENING_HOURS = urllib.parse.quote('web.gencat.cat/ca/contacte/012/')
    print('http://' + OPENING_HOURS)
    print_phone_information()
