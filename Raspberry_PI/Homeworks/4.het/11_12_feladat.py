from sense_hat import SenseHat
from time import sleep
import random

o = (0,0,0)
b = (0,0,255)

one_img = [ o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o]

two_img = [ o,o,o,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,o,o,o]
three_img = [
            o,o,o,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,b,b,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,b,b,o,
            o,o,o,o,o,o,o,o]

four_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o]

five_img = [o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o]

six_img = [ o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o,
            o,o,o,o,o,o,o,o,
            o,b,b,o,o,b,b,o,
            o,b,b,o,o,b,b,o]

dice = [one_img,two_img,three_img,four_img,five_img,six_img]

def dice_animation():
    for i in range(30)
        random_face = random.randint(1,6)
        sense.set_pixels(dice[random_face-1])
        sleep(0.1)
                

def number_gen(event):
    if event.action == "pressed":
        dice_animation()
        val = random.randint(1,6)
        print(val)
        if val == 1:
            sense.set_pixels(one_img)
        elif val == 2:
            sense.set_pixels(two_img)
        elif val == 3:
            sense.set_pixels(three_img)
        elif val == 4:
            sense.set_pixels(four_img)
        elif val == 5:
            sense.set_pixels(five_img)
        elif val == 6:
            sense.set_pixels(six_img)
        sleep(2)
        sense.clear()
        
sense.stick.direction_up = sense.clear
sense.stick.direction_down = sense.clear
sense.stick.direction_left = sense.clear
sense.stick.direction_right = sense.clear
sense.stick.direction_middle = number_gen


while True:
    pass