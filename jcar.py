import pygame
import sys
import math

pygame.init()
pygame.display.set_caption("Moving Car in Pygame")

WIDTH, HEIGHT = 1024, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("malgungothic", 24) 
move_sound = pygame.mixer.Sound('sound/move.mp3')


class Car:
    def __init__(self, image, speed, X, Y):
        original_image = pygame.image.load(f'images/{image}')
        self.original_image = pygame.transform.scale(original_image, (original_image.get_width()*0.9, original_image.get_height()*0.9))
        self.image = self.original_image
        self.location = self.image.get_rect(center=(X, Y))
        self.speed = 0
        self.angle = 90
        self.direction="stop"

    def rotate(self):
        # 이미지 회전 (시계 반대 방향으로 회전)
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.location = self.image.get_rect(center=self.location.center)

    def move(self):
        # 라디안으로 각도 변환
        if car.direction=="stop":
            self.speed =0
            move_sound.stop()
        if car.direction=="forward":
            self.speed +=1 
            move_sound.play()

        if car.direction=="back": 
            self.speed -=0.5
            move_sound.stop()

         # 예상 위치 계산
        radians = math.radians(self.angle)
        new_x = self.location.x + self.speed * math.cos(radians)
        new_y = self.location.y - self.speed * math.sin(radians)

        # 화면 경계 검사
        if 0 <= new_x <= WIDTH - self.location.width and 0 <= new_y <= HEIGHT - self.location.height:
            self.location.x = new_x
            self.location.y = new_y
        else:
            self.speed = 0
        

car = Car('carA1.png', 1, WIDTH/2, HEIGHT-100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            match (event.key):
                case (pygame.K_LEFT):
                    car.angle += 10  # 왼쪽으로 회전
                case (pygame.K_RIGHT):
                    car.angle -= 10  # 오른쪽으로 회전
                case (pygame.K_UP):
                    car.direction="forward"
                case (pygame.K_DOWN):
                    car.direction="back"
                case (pygame.K_SPACE):
                    car.speed =0
                    car.direction="stop"
    car.move()
    car.rotate()

    screen.fill((255,255,255))
    screen.blit(car.image, car.location)
    screen.blit(font.render("speed = " + str(car.speed), True, (0,0,0)), (50, 50))

    pygame.display.update()
    pygame.time.Clock().tick(30)
