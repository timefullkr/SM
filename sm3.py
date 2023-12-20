import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 1024, 576
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Free Fall Simulation")

gravity = 9.8 / 10
restitution = 0.90  # 복원 계수
R = 20  # 공의 반지름

class Ball:
    def __init__(self, X, Y, DY, red, green, blue):
        self.x = X
        self.y = Y
        self.dy = DY
        self.red = red
        self.green = green
        self.blue = blue
        self.pause = True

    def move(self):
        # 위치 변화
        self.dy += gravity
        self.y += self.dy

       
        wall_bottom = self.y + R > HEIGHT

        # 충돌 처리
        if wall_bottom:  # 아래쪽 벽 충돌
            self.y = HEIGHT - R
            self.dy *= -restitution

    def display(self):
        pygame.draw.ellipse(screen, (self.red, self.green, self.blue), (self.x - R, self.y - R, R * 2, R * 2))


# 클래스 인스턴스 생성
def _balls(cnt):
    balls = []
    for i in range(cnt):
        red = random.randint(0, 255)  # 0~255 사이 임의 정수 발생
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        X = random.randint(R, WIDTH - R)
        Y = random.randint(R, HEIGHT/2)
        balls.append(Ball(X, Y, 0, red, green, blue))  # 초기 속도는 0
    return balls


ball = _balls(100)
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
                ball = _balls(100)

    screen.fill((220, 220, 220))

    for b in ball:
        if not b.pause:
            b.move()
        b.display()

    pygame.display.flip()
    pygame.time.Clock().tick(30)
