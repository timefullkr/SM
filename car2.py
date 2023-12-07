import pygame
import sys

pygame.init()
pygame.display.set_caption("Moving Car in Pygame")
# Pygame 초기화
pygame.init()
# 상수들
WIDTH, HEIGHT = 1024, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("malgungothic", 24) 
pygame.display.set_caption("Physics Simulation")

# Load the image
# car_image = pygame.image.load('images/car.png')  # Make sure 'car.png' is in your project directory
# car_rect = car_image.get_rect()

class Car:
    def __init__(self, X, Y, MX, MY,image,speed):
            self.x=X
            self.y=Y
            self.mx=MX
            self.my=MY
            self.image = pygame.image.load(f'images/{image}')
            self.body = self.image.get_rect()
            self.width=self.body.width
            self.height=self.body.height
            self.speed = speed

    def move(self):
        # 위치 변화
        self.body.x += self.mx
        self.body.centery -= self.speed

# Initial position of the car
car =Car(0,HEIGHT,0,0,'car.png',10)
# car_rect.x = 0
# car_rect.centery = screen.get_height()

car.body.centerx = WIDTH/2
car.body.centery = HEIGHT
# Car speed
car_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    car.move()

   
    # Display the car
    screen.blit(car.image, car.body)

    pygame.display.update()
    pygame.time.Clock().tick(1)
