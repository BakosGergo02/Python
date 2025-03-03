fromt sense_hat import SenseHat

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

sense.set_pixels(heart_pixels)
