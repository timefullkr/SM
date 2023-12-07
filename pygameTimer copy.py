import pygame
import sys

pygame.init()
pygame.display.set_caption("Moving Car in Pygame")
screen = pygame.display.set_mode((800, 600))

# Load the image
car_image = pygame.image.load('images/car.png')  # Make sure 'car.png' is in your project directory
car_rect = car_image.get_rect()

# Initial position of the car
car_rect.x = 0
car_rect.centery = screen.get_height() / 2

# Car speed
car_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    # Move the car
    car_rect.x += car_speed

    # Reset position if the car moves off the screen
    if car_rect.x > screen.get_width():
        car_rect.x = -car_rect.width

    # Display the car
    screen.blit(car_image, car_rect)

    pygame.display.update()
    pygame.time.Clock().tick(30)
