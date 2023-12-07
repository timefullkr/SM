import pygame
import sys

pygame.init()
pygame.display.set_caption("Pygame Timer")
screen = pygame.display.set_mode((800, 600))
font = pygame.font.SysFont("malgungothic", 80) # 시스템 폰트 사용 시

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit( font.render("Timer : 0", True, (255, 255, 255)), [150, 200])

    pygame.display.update()
    pygame.time.Clock().tick(30)
        
