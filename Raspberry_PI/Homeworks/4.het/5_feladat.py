from random import randint
from sense_hat import SenseHat
from time import sleep

def random_colour():
     random_red = randint(0, 255)
     random_green = randint(0, 255)
     random_blue = randint(0, 255)
     return (random_red, random_green, random_blue)
    
sense.show_letter("G", random_colour())
sleep(1)
sense.show_letter("E", random_colour())
sleep(1)
sense.show_letter("R", random_colour())
sleep(1)
sense.show_letter("G", random_colour())
sleep(1)
sense.show_letter("Ő", random_colour())
sense.clear()