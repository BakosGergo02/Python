from sense_hat import SenseHat
from time import sleep

w = (255,255,255)
r = (255,0,0)

up_arrow =[
     w, w, w, r, r, w, w, w,
     w, w, r, r, r, r, w, w,
     w, r, r, r, r, r, r, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w]
down_arrow =[
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, r, r, w, w, w,
     w, r, r, r, r, r, r, w,
     w, w, r, r, r, r, w, w,
     w, w, w, r, r, w, w, w]
right_arrow =[
     w, w, w, w, w, w, w, w,
     w, w, w, w, w, r, w, w,
     w, w, w, w, w, r, r, w,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     w, w, w, w, w, r, r, w,
     w, w, w, w, w, r, w, w,
     w, w, w, w, w, w, w, w]
left_arrow =[
     w, w, w, w, w, w, w, w,
     w, w, r, w, w, w, w, w,
     w, r, r, w, w, w, w, w,
     r, r, r, r, r, r, r, r,
     r, r, r, r, r, r, r, r,
     w, r, r, w, w, w, w, w,
     w, w, r, w, w, w, w, w,
     w, w, w, w, w, w, w, w]

middle = [
     w, w, w, w, w, w, w, w,
     w, w, w, w, w, w, w, w,
     w, w, w, r, r, w, w, w,
     w, w, r, r, r, r, w, w,
     w, w, r, r, r, r, w, w,
     w, w, w, r, r, w, w, w,
     w, w, w, w, w, w, w, w,
     w, w, w, w, w, w, w, w]


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
             if event.direction == "up":
                 sense.set_pixels(up_arrow) # Up arrow
             elif event.direction == "down":
                 sense.set_pixels(down_arrow) # Down arrow
             elif event.direction == "left":
                 sense.set_pixels(left_arrow) # Left arrow
             elif event.direction == "right":
                 sense.set_pixels(right_arrow) # Right arrow
             elif event.direction == "middle":
                 sense.set_pixels(middle) # Enter key
             sleep(0.5)
             sense.clear()
            
