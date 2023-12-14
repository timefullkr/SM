import pygame
import sys

pygame.init()
pygame.display.set_caption("Pygame Timer")
screen = pygame.display.set_mode((200, 100))
font = pygame.font.SysFont("malgungothic", 30) 

cnt = 0
last_update_time = 0 
while True:
    # 현재 시간을 밀리초 단위로 가져옴
    current_time = pygame.time.get_ticks()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    if current_time - last_update_time > 1000:
       cnt +=1; last_update_time = current_time  
 
    screen.fill((0, 0, 0))
    screen.blit(font.render(
                        f"Timer : {cnt}",
                        True,
                        (255, 255, 255)
                        ),
                        [30,30]
                )

    pygame.display.update()
    pygame.time.Clock().tick(30)
