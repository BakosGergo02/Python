from sense_hat import SenseHat
from time import sleep


w = (255,255,255)
r = (255,0,0)

heart_pixels = [
     w, w, w, w, w, w, w, w,
     w, r, r, w, w, r, r, w,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     w, r, r, r, r, r, r, w,
     w, w, r, r, r, r, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, w, w, w, w, w]

#sense.set_pixels(heart_pixels)

def red():
    sense.set_pixels(heart_pixels)
    sleep(0.5)
    sense.set_pixels(heart_pixels)
    sleep(0.5)
    sense.set_pixels(heart_pixels)
    sense.clear()
def blue():
    sense.clear(0, 0, 255)
def green():
    sense.clear(0, 255, 0)
def yellow():
    sense.clear(255, 255, 0)
    
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

while True:
    pass
