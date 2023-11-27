import pygame
import math
import sys

# Pygame 초기화
pygame.init()

# 상수들
WIDTH, HEIGHT = 1024, 576
gravity = 9.8/10  # 중력 가속도. 스케일은 1:10 - 0.2만큼 줄어듦
restitution = 0.7  # 복원 계수
R = 10  # 공의 반지름
X, Y = R, HEIGHT - R  # Starting position (x, y) - 바닥에서 시작
angle = 45  # 출발 각도
speed = 37  # 공의 속도
floor_friction = 0.9  # 바닥 마찰 계수

# 속도 계산
dx = speed * math.cos(math.radians(angle))  # x 축의 속도
dy = -speed * math.sin(math.radians(angle))  # y 축의 속도

#speed - 한번에 나가는 거리 - 37

# 디스플레이 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")


# 클래스
class Ball:
    def __init__(self, X, Y, W, H, DX, DY):
        self.x, self.y, self.w, self.h, self.dx, self.dy = X, Y, W, H, DX, DY

#self - ball 자신


    def move(self):
        # 위치 변화
        self.dy += gravity
        self.x += self.dx
        self.y += self.dy

        # 왼쪽 & 오른쪽 벽 충돌
        if self.x + self.w/2 > WIDTH:
            self.x = WIDTH - self.w/2
            self.dx *= -restitution
        elif self.x - self.w/2 < 0:
            self.x = self.w/2
            self.dx *= -restitution

        # 위 & 아래 벽 충돌
        if self.y + self.h/2 > HEIGHT:
            self.y = HEIGHT - self.h/2
            self.dy *= -restitution
            self.dx *= floor_friction  # 바닥 마찰 계수 적용
        elif self.y - self.h/2 < 0:
            self.y = self.h/2
            self.dy *= -restitution

    def display(self):
        pygame.draw.ellipse(screen, (0, 0, 0, 192), (self.x - self.w/2, self.y - self.h/2, self.w, self.h))


# 클래스 인스턴스 생성
ball = Ball(X, Y, R*2, R*2, dx, dy)

# 메인 루프 - 창 닫기 전까지 반복
running = True
index=0
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False  

    # if index==1 :
    #     continue 
    #위에거 풀면 한번 출발하고 멈춤(speed까지 도착 후 멈춤)
    screen.fill((220, 220, 220))
    
    ball.move()
    ball.display()

    # 화면 갱신
    pygame.display.flip()
    pygame.time.Clock().tick(30) # 1초에 30번씩 업데이트
    index +=1
   
# 정리
pygame.quit()
sys.exit()