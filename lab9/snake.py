import pygame, random, time
pygame.init()
RED, GREEN, BLUE = (255, 0, 0), (0, 255, 0), (0, 0, 255)
width, height = 800, 600
colors_of_fruit = [RED, GREEN, BLUE]

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

#variables and their initialization
score = 0
fruit_eaten = False
fr_x, fr_y = random.randrange(0, width, 20), random.randrange(0, height, 20)
fruit_coor = [fr_x, fr_y]
fruit_weight = random.randint(1, 3)
fruit_color = colors_of_fruit[fruit_weight - 1]
fime = time.time()
lvl = 1.0
head_square = [100, 100]
squares = [[20, 100], [40, 100], [60, 100], [80, 100], [100, 100]]
direction, next_dir = "right", "right"
done = False

def game_over(font, size, color):
    global done
    g_o_font = pygame.font.SysFont(font, size)
    g_o_surface = g_o_font.render("Game Over! your score: " + str(score), True, color)
    screen.fill('red')
    screen.blit(g_o_surface, (125, 255))
    pygame.display.update()
    pygame.time.delay(2000)
    done = True

#start of gameplay loop
while not done:
    #gameplay even conditions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                next_dir = "down"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                next_dir = "up"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                next_dir = "left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                next_dir = "right"
    for square in squares[:-1]:
        if head_square[0] == square[0] and head_square[1] == square[1]:
            game_over("times new roman", 50, (128, 128, 128))


    #scene logic
    if next_dir == "right" and direction != "left":
        direction = "right"
    if next_dir == "up" and direction != "down":
        direction = "up"
    if next_dir == "left" and direction != "right":
        direction = "left"
    if next_dir == "down" and direction != "up":
        direction = "down"


    #wall and moving
    if direction == "right":
        if head_square[0] + 20 < 800:
            head_square[0] += 20
        else:
            game_over("times new roman", 50, (128, 128, 128))
    if direction == "left":
        if head_square[0] - 20 > -1:
            head_square[0] -= 20
        else:
            game_over("times new roman", 50, (128, 128, 128))
    if direction == "up":
        if head_square[1] - 20 > -1:
            head_square[1] -= 20
        else:
            game_over("times new roman", 50, (128, 128, 128))
    if direction == "down":
        if head_square[1] + 20 < 600:
            head_square[1] += 20
        else:
            game_over("times new roman", 50, (128, 128, 128))
    
    # eating
    if head_square[0] == fruit_coor[0] and head_square[1] == fruit_coor[1]:
        fruit_eaten = True
        score += 10 * fruit_weight
    lvl = score // 40

    new_square = [head_square[0], head_square[1]]
    squares.append(new_square)
    if not fruit_eaten:
        squares.pop(0)

    if (time.time() - fime) >= 18 / fruit_weight:
        fime = time.time()
        fruit_eaten = True

    if fruit_eaten:
        fime = time.time()
        fr_x = random.randrange(0, width, 20)
        fr_y = random.randrange(0, height, 20)
        fruit_coor = [fr_x, fr_y]
        fruit_weight = random.randint(1, 3)
        fruit_color = colors_of_fruit[fruit_weight - 1]
        fruit_eaten = False


    #drawing section
    screen.fill((0, 0, 0))

    score_font = pygame.font.SysFont("times new roman", 20)
    score_surface = score_font.render("Score: " + str(score) + ", lvl: " + str(int(lvl)), True, (128, 128, 128))
    score_rect = score_surface.get_rect()
    
    screen.blit(score_surface, score_rect)

    if not fruit_eaten:
        pygame.draw.circle(screen, fruit_color, (fruit_coor[0] + 10, fruit_coor[1] + 10), 10)

    for el in squares:
        pygame.draw.rect(screen, (0, 127, 0),
                         pygame.Rect(el[0], el[1], 20, 20))

    pygame.display.flip()
    pygame.time.Clock().tick(3 + lvl)

pygame.quit()