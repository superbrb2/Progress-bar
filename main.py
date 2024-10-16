import pygame, sys
from ProgressBar import ProgressBar

screen_width = screen_height = 700

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

bar1 = ProgressBar(200,200,(100,50),400,50)
bar2 = ProgressBar(200,12,(100,150),400,50)
bar3 = ProgressBar(100,50,(100,250),300,100)
bar4 = ProgressBar(200,175,(100,375),200,25)
bar4.add_bar_queue(-100)
bar4.add_bar_queue(50)
bar4.add_bar_queue(-100)
bar4.add_bar_queue(100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('grey')

    bar1.update(screen)
    bar2.update(screen)
    bar3.update(screen)
    bar4.update(screen)

    pygame.display.update()
    clock.tick(60)
