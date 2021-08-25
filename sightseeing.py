"""
Sightseeing file
"""
# ****************************************
# Authorship:
# Jordi Planes Cid
# Marc Cervera Rosell
# Polytecnich school - University of Lleida
# ****************************************
import subprocess
import urllib
import colors


def sightseeing_lleida():
    """
    This function prints the most important places of Lleida and the gastronomy
    """
    print(colors.Color.BLUE + "Link to the Lleida tourist office" + colors.Color.END)
    tourism_office = urllib.parse.quote('www.turismedelleida.cat/')
    print('https://' + tourism_office)
    print(colors.Color.YELLOW + "Most important places of Lleida" + colors.Color.END)
    print(colors.Color.YELLOW + "Gastronomy of Lleida" + colors.Color.END)
    subprocess.call('./print_pictures.sh')
