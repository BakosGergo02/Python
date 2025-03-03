from sense_hat import SenseHat
import time
sense = SenseHat()

p = [2,3]
light_len = 3
space_size = 8
speed = 1/7

r = (255,0,0)
n = (0,0,0)

space = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]
def shift_right():
    global p, space
    if p[0] + light_len < space_size:
        for i in range(light_len):
            space[3 * space_size + p[0] + i] = n  
        p[0] += 1  

        for i in range(light_len):
            space[3 * space_size + p[0] + i] = r  
        sense.set_pixels(space)

def shift_left():
    global p, space
    if p[0] > 0:
        for i in range(light_len):
            space[3 * space_size + p[0] + i] = n  
        p[0] -= 1  

       
        for i in range(light_len):
            space[3 * space_size + p[0] + i] = r 
        
        sense.set_pixels(space)

def main():
    global p
    while True:
  
        while p[0] <= space_size - light_len - 1:
            shift_right()
            time.sleep(speed)
        while p[0] > 0: 
            shift_left()
            time.sleep(speed)
   
   
if __name__ == "__main__":
    main()
