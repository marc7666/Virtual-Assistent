"""
Phone payment file
"""
import urllib
import colors


def print_phone_information():
    """
    This method prints the 012 phone information.
    """
    file = open('012_information.txt', 'r')
    content = file.read()
    print(colors.Color.GREEN + content + colors.Color.END)
    file.close()


def cat_012():
    """
    This function prints the information of 012 telephone
    """
    print(colors.Color.BLUE + "Check the 012 opening hours:" + colors.Color.END)
    opening_hours = urllib.parse.quote('web.gencat.cat/ca/contacte/012/')
    print('http://' + opening_hours)
    print_phone_information()
