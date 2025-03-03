from sense_hat import SenseHat
import time
sense = SenseHat()

state = 0
synch = False

w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

patterns = {
    0: [
        n, n, n, r, r, n, n, n,
        n, n, n, r, r, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ],
    1: [
        n, n, n, r, r, n, n, n,
        n, n, n, r, r, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ],
    2: [
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, g, g, n, n, n,
        n, n, n, g, g, n, n, n
    ],
    3: [
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ]
}


def display_state(state, duration):
    sense.set_pixels(patterns[state])
    time.sleep(duration)
    sense.clear()

def out_of_order_state():
 sense.set_pixels(patterns[3])
 time.sleep(0.5)
 sense.clear()
 time.sleep(0.5)
 
def set_state():
  global state
  # state variable has been defined outside
  if state < 3:
   state += 1
  else:
    state = 0

def button_event(event):
 global state, synch
 if event.action == 'released':
   if synch:
     synch = False
     sense.clear()
   else:
     synch =True
     state = 3


sense.stick.direction_middle = button_event

def main():
  global state,synch
  while True:
    if not synch:
        durations = [3, 1, 2, 1]
        display_state(state, durations[state])
        set_state()
    else:
      out_of_order_state()

if __name__ == "__main__":
    main()
