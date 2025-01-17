import pygame
import sys
from control import move_forward, move_backward, turn_left, turn_right

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Key Press Detection")

# Define key press durations
SHORT_PRESS_DURATION = 500  # milliseconds
LONG_PRESS_DURATION = 1000  # milliseconds


key_press_start_times = {}

keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]


def startRun(key: int):
    if key == pygame.K_UP:
        move_forward()
    elif key == pygame.K_DOWN:
        move_backward()
    elif key == pygame.K_LEFT:
        turn_left()
    elif key == pygame.K_RIGHT:
        turn_right()


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key_press_start_times[event.key] = pygame.time.get_ticks()
            if event.key in keys:
                startRun(event.key)
        elif event.type == pygame.KEYUP:
            press_duration = pygame.time.get_ticks() - key_press_start_times.get(
                event.key, 0
            )
            print("KeyUp", event.key)
            # if press_duration < SHORT_PRESS_DURATION:
            #   print(f"Key {pygame.key.name(event.key)} was short pressed")
            # elif press_duration >= LONG_PRESS_DURATION:
            #   print(f"Key {pygame.key.name(event.key)} was long pressed")
            key_press_start_times.pop(event.key, None)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
