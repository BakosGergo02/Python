import time
import random
from sense_hat import SenseHat
from signal import pause

# Initialize Sense HAT
sense = SenseHat()

# Define colors
SNAKE_COLOR = (0, 255, 0)   # Green
FOOD_COLOR = (255, 0, 0)    # Red
BACKGROUND_COLOR = (0, 0, 0) # Black

# Define initial snake properties
snake = [(4, 4)]
snake_direction = (0, 1)  # Initial direction: right
food_position = (0, 0)
game_over = False

# Place the initial food
def place_food():
    while True:
        new_food = (random.randint(0, 7), random.randint(0, 7))
        if new_food not in snake:
            return new_food

food_position = place_food()

# Update the display
def draw_snake():
    sense.clear(BACKGROUND_COLOR)  # Clear screen
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], SNAKE_COLOR)
    sense.set_pixel(food_position[0], food_position[1], FOOD_COLOR)

# Change direction based on joystick input
def change_direction(event):
    global snake_direction
    if event.action == 'pressed':
        if event.direction == 'up' and snake_direction != (0, 1):
            snake_direction = (0, -1)
        elif event.direction == 'down' and snake_direction != (0, -1):
            snake_direction = (0, 1)
        elif event.direction == 'left' and snake_direction != (1, 0):
            snake_direction = (-1, 0)
        elif event.direction == 'right' and snake_direction != (-1, 0):
            snake_direction = (1, 0)

sense.stick.direction_up = change_direction
sense.stick.direction_down = change_direction
sense.stick.direction_left = change_direction
sense.stick.direction_right = change_direction

# Main game loop
while not game_over:
    # Calculate new head position
    new_head = (snake[0][0] + snake_direction[0],
                snake[0][1] + snake_direction[1])

    # Check for collisions with screen border
    if new_head[0] < 0 or new_head[0] > 7 or new_head[1] < 0 or new_head[1] > 7:
        game_over = True
        break

    # Check for collisions with self
    if new_head in snake:
        game_over = True
        break

    # Move snake
    snake.insert(0, new_head)

    # Check if food is eaten
    if new_head == food_position:
        food_position = place_food()
    else:
        snake.pop()  # Remove last segment if no food eaten

    # Update the display
    draw_snake()

    # Delay to control speed
    time.sleep(0.3)

# Game Over display
sense.show_message("Game Over", text_colour=(255, 0, 0))
sense.clear()
