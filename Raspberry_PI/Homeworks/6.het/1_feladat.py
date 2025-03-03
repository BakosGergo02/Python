from sense_hat import SenseHat
import time
sense = SenseHat()
delay_val = 1.0

w = (255,255,255)
n = (0,0,0)

on = [
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w,
 w, w, w, w, w, w, w, w
 ]

off = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

def delay_middle(event):
  global delay_val
  # delay_val is a global variable because it
  # has been defined outside of this function
  if event.action == 'pressed':
   delay_val = 0.2
  elif event.action == 'released':
   delay_val = 1.0
   
def delay_down(event):
  global delay_val
  # delay_val is a global variable because it
  # has been defined outside of this function
  if event.action == 'pressed':
   delay_val = 2.0
  elif event.action == 'released':
   delay_val = 1.0
   
def delay_up(event):
  global delay_val
  # delay_val is a global variable because it
  # has been defined outside of this function
  if event.action == 'pressed':
   delay_val = 0.5
  elif event.action == 'released':
   delay_val = 1.0

def delay_left(event):
  global delay_val
  # delay_val is a global variable because it
  # has been defined outside of this function
  if event.action == 'pressed':
   delay_val = 3.0
  elif event.action == 'released':
   delay_val = 1.0

def delay_right(event):
  global delay_val
  # delay_val is a global variable because it
  # has been defined outside of this function
  if event.action == 'pressed':
   delay_val = 0.1
  elif event.action == 'released':
   delay_val = 1.0

sense.stick.direction_middle = delay_middle
sense.stick.direction_down = delay_down
sense.stick.direction_up = delay_up
sense.stick.direction_left = delay_left
sense.stick.direction_right = delay_right


while True:
 sense.set_pixels(on)
 time.sleep(delay_val)
 sense.set_pixels(off)
 time.sleep(delay_val)
