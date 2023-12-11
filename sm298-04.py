import pygame
import math
import sys
import time  
import pygame_gui
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


# 속도 계산
dx = speed * math.cos(math.radians(angle))  # x 축의 속도
dy = -speed * math.sin(math.radians(angle))  # y 축의 속도

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("malgungothic", 24) 
pygame.display.set_caption("Physics Simulation")

# 클래스 
class Ball:
    def __init__(self, X, Y, DX, DY):
        self.x=X
        self.y=Y
        self.dx=DX
        self.dy=DY
        self.distance=0
        self.stop=True

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
                if ball.distance==0 :
                    ball.distance=self.x
                    print(f"distance :{self.x:.2f}")

            case (_, _, _, True):  # 위쪽 벽 충돌
                self.y = R
                self.dy *= -restitution
            case _:
                pass  # 충돌이 없는 경우


    def display(self):
        pygame.draw.ellipse(screen, (0, 0, 0, 192), (self.x -R, self.y - R, R*2, R*2))



ball = Ball(X, Y,  dx, dy)
screen.fill((220, 220, 220))
ball.display()
pygame.display.flip()

running = True
print(  ball.stop)
while running:
    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(" Press ascii code=",event.key )
            if event.key == pygame.K_SPACE:
                ball.stop = not ball.stop

    

    screen.fill((220, 220, 220))
    if not ball.stop:
        ball.move()

    ball.display()
    screen.blit(font.render("distance = " + str(ball.distance), True, (255, 0, 0)), (50, 50))
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()

# 