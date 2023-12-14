import pygame
import math
import sys
import random

pygame.init()
WIDTH, HEIGHT = 1024, 576
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")

gravity = 9.8 / 10
restitution = 0.7  # 복원 계수
friction_coefficient = 0.6
R = 20  # 공의 반지름
angle = 45  # 출발 각도
speed = 28  # 공의 속도

dx = speed * math.cos(math.radians(angle)) 
dy = -speed * math.sin(math.radians(angle))

class Ball:
    def __init__(self, X, Y, DX, DY, red, green, blue):
        self.x = X
        self.y = Y
        self.dx = DX
        self.dy = DY
        self.red = red
        self.green = green
        self.blue = blue
        self.pause = True

    def move(self):
        # 위치 변화
        self.dy += gravity
        self.x += self.dx
        self.y += self.dy

        # 충돌 조건 계산
        wall_right = self.x + R > WIDTH
        wall_left = self.x - R < 0
        wall_bottom = self.y + R > HEIGHT
        wall_top = self.y - R < 0

        # 충돌 처리
        match (wall_left,wall_right,wall_top, wall_bottom ):
            case (True, _, _, _):  # 왼쪽 벽 충돌
                self.x = R
                self.dx *= -restitution
            case (_, True, _, _):  # 오른쪽 벽 충돌
                self.x = WIDTH - R
                self.dx *= -restitution
            case (_, _, True,_):  # 위쪽 벽 충돌
                self.y = R
                self.dy *= -restitution
            case (_, _, _,True):  # 아래쪽 벽 충돌
                self.y = HEIGHT - R
                self.dy *= -restitution
                self.dx *= friction_coefficient
            
            case _:
                pass  # 충돌이 없는 경우

    def display(self):
        pygame.draw.ellipse(screen, (self.red, self.green, self.blue), (self.x - R, self.y - R, R * 2, R * 2))


# 클래스 인스턴스 생성
def initialize_balls(cnt):
    balls = []
    ball_cnt = cnt
    for i in range(ball_cnt):
        red = random.randint(0, 255)  # 0~255 사이 난수 발생
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        X = random.randint(R, WIDTH - R)
        Y = random.randint(R, HEIGHT - R)
        balls.append(Ball(X, Y, dx, dy, red, green, blue))
    return balls


ball = initialize_balls(100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(len(ball)):
                    ball[i].pause = not ball[i].pause
            if event.key == pygame.K_F9:  # F9 키를 눌렀을 때
                ball = initialize_balls(100)

    screen.fill((220, 220, 220))

    for b in ball:
        if not b.pause:
            b.move()
        b.display()

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
