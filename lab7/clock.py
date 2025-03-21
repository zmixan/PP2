import pygame
import datetime

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1100, 800))
pygame.display.set_caption("Mickey's Clock")
screen.fill("White")

bckgrnd = pygame.image.load("clock.png")
bckgrnd = pygame.transform.scale(bckgrnd, (1050, 800))
p_hand = pygame.image.load("min_hand.png")
p_hand = pygame.transform.scale(p_hand, (1050, 800))
l_hand = pygame.image.load("sec_hand.png")
l_hand = pygame.transform.scale(l_hand, (1050, 800))

center = (535, 400)

run = True
while run:
    clock.tick(60)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
    
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second

    anglefs = -6 * second + 57
    anglefm = -6 * minute - 47

    rotated_sec = pygame.transform.rotate(l_hand, anglefs)
    rotated_min = pygame.transform.rotate(p_hand, anglefm)

    sec_pos = (center[0] - rotated_sec.get_width() // 2, center[1] - rotated_sec.get_height() // 2)
    min_pos = (center[0] - rotated_min.get_width() // 2, center[1] - rotated_min.get_height() // 2)

    screen.blit(bckgrnd, (10, 0))
    screen.blit(rotated_sec, sec_pos)
    screen.blit(rotated_min, min_pos)

    pygame.display.update()

pygame.quit()
