import pygame
import math
import sys
import time
import random
# Pygame 초기화
pygame.init()

# 화면 크기 
WIDTH, HEIGHT = 1024, 576
gravity = 9.8/10  # 중력 가속도. 스케일은 1:10
restitution = 0.7  # 복원 계수
bb=0.6

R = 20  # 공의 반지름
X, Y = R, HEIGHT-R # Starting position (x, y)
angle = 45  # 출발 각도
speed = 28  # 공의 속도

# 속도 계산
dx = speed * math.cos(math.radians(angle))  # x 축의 속도
dy = -speed * math.sin(math.radians(angle))  # y 축의 속도

# 디스플레이 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Simulation")


# 클래스
class Ball:
    def __init__(self, X, Y,  DX, DY,red,green,blue):
         self.x=X
         self.y=Y
         self.dx=DX
         self.dy=DY
         self.red=red
         self.green=green
         self.blue=blue
         self.pause=True
         self.dd=0
         

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
                self.dx *= bb
                if self.dd==0:
                    self.dd=self.x
                    print( "거리=", self.x )
                
            case (_, _, _, True):  # 위쪽 벽 충돌
                self.y = R
                self.dy *= -restitution
            case _:
                pass  # 충돌이 없는 경우


    def display(self):
        pygame.draw.ellipse(screen, (self.red,self.green,self.blue), (self.x - R, self.y - R, R*2, R*2))

# 클래스 인스턴스 생성b

ball=[]
for i in range(4):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    ball.append( Ball( X + i*100, Y, dx, dy, red, green,blue ))

running = True
while running:

    for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                running = False  
            if event.type == pygame.KEYDOWN:
                print(" Press ascii code=",event.key )
                if event.key==32:
                    for i in range(4):
                       ball[i].pause= not ball[i].pause   
                  
    screen.fill((220, 220, 220))
    
    for i in range(4):
        if ball[i].pause ==False :
            ball[i].move()
        
        ball[i].display()
   
   

    # 화면 갱신
    pygame.display.flip()
    pygame.time.Clock().tick(30)
    
    

pygame.quit()
sys.exit()

# 1. SPACE 키를 누르면 시작 OR 정지
# 2. 코드 분석 >> 자신의 코드로 만들기
# 2.1  class Ball 분석 정리 -> 불필요한 내용 제거 단순화 
# 2.2  def move(self)의 IF 문을  match 문으로 변경 충돌 조건을 더 명확하게 표현 하고, 가독성 향상