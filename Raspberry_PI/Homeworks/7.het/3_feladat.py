from sense_hat import SenseHat
import random
from time import sleep

# Initialize Sense HAT and define game settings
sense = SenseHat()
speed = 0.3  # Initial ball speed
bat = [7, 3]  # Initial position of the bat (centered on the bottom row)
score = 0  # Score tracking
up_down = -1  # Ball direction (1 for down, -1 for up)

# Define colors
w = (0, 0, 0)       # White (background)
r = (255, 0, 0)     # Red (ball)
b = (0, 0, 255)     # Blue (bat)

# Initialize game space
game_space = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, b, b, b, w, w
]

# Update the display with the current game state
def update_space(x, y, colour):
    p = 8 * x + y  # Convert coordinates to index
    game_space[p] = colour
    sense.set_pixels(game_space)

# Move the bat to the left
def left(event):
    global bat
    if event.action == 'pressed':
        # Prevent bat from moving off the left edge
        if bat[1] > 1:
            update_space(bat[0], bat[1] + 1, w)  # Clear rightmost pixel of bat
            bat[1] -= 1  # Move bat left
            update_space(bat[0], bat[1] - 1, b)  # Set new leftmost pixel of bat

# Move the bat to the right
def right(event):
    global bat
    if event.action == 'pressed':
        # Prevent bat from moving off the right edge
        if bat[1] < 5:
            update_space(bat[0], bat[1] - 1, w)  # Clear leftmost pixel of bat
            bat[1] += 1  # Move bat right
            update_space(bat[0], bat[1] + 1, b)  # Set new rightmost pixel of bat

# Set up joystick controls
sense.stick.direction_left = left
sense.stick.direction_right = right

# Initialize game
sense.clear()
sense.set_pixels(game_space)
game_alive = True

# Define the initial position and direction of the ball
x = 0  # Ball starts at the top row
y = random.randint(0, 7)  # Ball's starting column
d = random.choice([-1, 1])  # Horizontal direction (left or right)
update_space(x, y, r)

# Main game loop
while game_alive:
    sleep(speed)
    update_space(x, y, w)  # Clear current ball position

    # Check if the ball hits the bat
    if x == 6 and up_down == 1:
        if bat[1] <= y <= bat[1] + 2:
            # Ball bounces off the bat
            up_down = -1
            score += 1
        else:
            # Ball missed the bat; game over
            game_alive = False
            break

    # Check if the ball reaches the top
    if x == 0 and up_down == -1:
        up_down = 1  # Ball starts moving downward

    # Ball reaches the right side of the grid
    if y == 7 and d == 1:
        d = -1  # Reverse direction to the left
    # Ball reaches the left side of the grid
    elif y == 0 and d == -1:
        d = 1  # Reverse direction to the right

    # Update ball position
    y += d
    x += up_down
    update_space(x, y, r)  # Update display with new ball position

# Game over message and score display
sense.clear()
sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
sense.show_message("Score: " + str(score), scroll_speed=0.05, back_colour=w)
