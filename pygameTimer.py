import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Pygame Timer")
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("malgungothic", 80) # 시스템 폰트 사용 시
tmr = 0
while True:
    tmr = tmr + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    screen.blit( font.render("타임머 : " + str(tmr), True, WHITE), [100, 200])
    pygame.display.update()
    pygame.time.Clock().tick(1)
        
