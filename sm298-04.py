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
# 1. 클래스 변경

# 클래스 
class Ball:
    def __init__(self, X, Y, DX, DY):
        self.x=X
        self.y=Y
        self.dx=DX
        self.dy=DY

    def move(self):
        # 위치 변화
        self.dy += gravity
        self.x += self.dx
        self.y += self.dy

        # 충돌 조건 계산
        collide_right = self.x + R > WIDTH
        collide_left = self.x - R < 0
        collide_bottom = self.y + R > HEIGHT
        collide_top = self.y - R < 0

        # 충돌 처리
        match (collide_right, collide_left, collide_bottom, collide_top):
            case (True, _, _, _):  # 오른쪽 벽 충돌
                self.x = WIDTH - R
                self.dx *= -restitution
            case (_, True, _, _):  # 왼쪽 벽 충돌
                self.x = R
                self.dx *= -restitution
            case (_, _, True, _):  # 아래쪽 벽 충돌
                self.y = HEIGHT - R
                self.dy *= -restitution
                self.dx *= floor_friction  # 바닥 마찰 계수 적용
            case (_, _, _, True):  # 위쪽 벽 충돌
                self.y = R
                self.dy *= -restitution
            case _:
                pass  # 충돌이 없는 경우


    def display(self):
        pygame.draw.ellipse(screen, (0, 0, 0, 192), (self.x -R, self.y - R, R*2, R*2))


# 클래스 인스턴스 생성
# ball = Ball(X, Y, R*2, R*2, dx, dy)
ball = Ball(X, Y,  dx, dy)

# 메인 루프 - 창 닫기 전까지 반복
running = True
cnt=0
loop=False
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False  
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   print(" Press K_SPACE")
                   loop=True if loop !=True else False
   
    if loop==True:
        continue
    
    screen.fill((220, 220, 220))
    
    ball.move()
    ball.display()

    # 화면 갱신
    pygame.display.flip()
    pygame.time.Clock().tick(30) # 1초에 30번씩 업데이트
    cnt +=1
   
# 정리
pygame.quit()
sys.exit()