from PIL import Image
import os

import colors


def print_pictures():
    dir = '/home/marc/Escritorio/Virtual-Assistent/Pictures'
    imgList = os.listdir('/home/marc/Escritorio/Virtual-Assistent/Pictures')
    imgList.sort(key=lambda x: int(x.replace("frame", "").split('.')[0]))
    for count in range(0, len(imgList)):
        im_name = imgList[count]
        im_path = os.path.join(dir, im_name)
        print(im_path)
    '''OLD_CATHEDRAL = Image.open("Seu Vella.jpg")
    print(colors.Color.GREEN + "Seu Vella (old cathedral)" + colors.Color.END)
    plt.imshow(OLD_CATHEDRAL)
    plt.show()
    OLD_ENTRANCE = Image.open("Arc del pont.jpg")
    print(colors.Color.GREEN + "Old entrance and Indíbil and Mandoni statue" + colors.Color.END)
    OLD_ENTRANCE.show()
    JEWISH_QUARTER = Image.open("Barri jueu.jpg")
    print(colors.Color.GREEN + "Jewish quarter" + colors.Color.END)
    JEWISH_QUARTER.show()
    NEW_CATHEDRAL = Image.open("Catedral nova.jpg")
    print(colors.Color.GREEN + "New cathedral" + colors.Color.END)
    NEW_CATHEDRAL.show()
    OLD_WATER_TANK = Image.open("Dipòsit.jpg")
    print(colors.Color.GREEN + "Old water tank" + colors.Color.END)
    OLD_WATER_TANK.show()
    MODERNIST_HOUSES = Image.open("Magi Llorens.jpg")
    print(colors.Color.GREEN + "Modernist houses (In the image we see the house of Magi Llorens)"
          + colors.Color.END)
    MODERNIST_HOUSES.show()
    PAERIA_PALACE = Image.open("Palau de la Paeria")
    print(colors.Color.GREEN + "Paeria palace (city town hall)"
          + colors.Color.END)
    PAERIA_PALACE.show()
    SAINT_JAMES_CHAPEL = Image.open("Peu del Romeu.jpg")
    print(colors.Color.GREEN + "Saint James chapel, Peu del Romeu" + colors.Color.END)
    SAINT_JAMES_CHAPEL.show()
    SAINT_JOHN = Image.open("Sant Joan.jpeg")
    print(colors.Color.GREEN + "Saint John church" + colors.Color.END)
    SAINT_JOHN.show()
    SAINT_LLORENÇ_CHURCH = Image.open("Sant Llorenç.jpg")
    print(colors.Color.GREEN + "Saint Llorenç church" + colors.Color.END)
    SAINT_LLORENÇ_CHURCH.show()
    OLD_SAINT_MARTIN = Image.open("Sant Martí la vella.jpg")
    print(colors.Color.GREEN + "Saint Martn old church" + colors.Color.END)
    OLD_SAINT_MARTIN.show()
    OLD_HOSPITAL = Image.open("Santa Maria antic.jpg")
    print(colors.Color.GREEN + "Old hospital of Santa Maria" + colors.Color.END)
    OLD_HOSPITAL.show()
    CASTLE = Image.open("Suda del rei.jpg")
    print(colors.Color.GREEN + "King's castle, Suda del rei" + colors.Color.END)
    CASTLE.show()'''
