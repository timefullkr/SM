import pygame
import math
import sys
import time  
# Pygame 초기화
pygame.init()
# 상수들
WIDTH, HEIGHT = 1024, 576
gravity = 9.8/10  # 중력 가속도. 스케일은 1:10 - 0.2만큼 줄어듦
restitution = 0.7  # 복원 계수
R = 10  # 공의 반지름
X, Y = R, HEIGHT - R  # Starting position (x, y) - 바닥에서 시작
angle = 45  # 출발 각도
speed = 30  # 공의 속도
floor_friction = 0.9  # 바닥 마찰 계수

dx = speed * math.cos(math.radians(angle))  # x 축의 속도
dy = -speed * math.sin(math.radians(angle))  # y 축의 속도

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 클래스 
class Ball:
    def __init__(self, X, Y, DX, DY):
        self.x=X
        self.y=Y
        self.dx=DX
        self.dy=DY
        self.pause=True
    def move(self):
        # 위치 변화
        self.dy += gravity
        self.x += self.dx
        self.y += self.dy

        # 왼쪽 & 오른쪽 벽 충돌
        if self.x + R > WIDTH:
            self.x = WIDTH - R
            self.dx *= -restitution
        elif self.x - R < 0:
            self.x = R
            self.dx *= -restitution
        # 상단 & 하단 벽 충돌
        if self.y + R > HEIGHT:
            self.y = HEIGHT - R
            self.dy *= -restitution
        elif self.y - R < 0:
            self.y = R
            self.dy *= -restitution


    def display(self):
        pygame.draw.ellipse(screen, (0, 0, 0, 192), (self.x -R, self.y - R, R*2, R*2))



ball = Ball(X, Y,  dx, dy)


running = True

while running:
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(" Press ascii code=",event.key )
            if event.key == pygame.K_SPACE:
                 ball.pause=True  if  ball.pause !=True  else False

    

    screen.fill((220, 220, 220))
    
    if not ball.pause:
        ball.move()

    ball.display()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()

# 