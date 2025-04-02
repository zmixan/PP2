#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
a = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
music = pygame.mixer_music.load("background.wav")
pygame.mixer.music.play(-1)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.active = False
        self.weight = random.randint(1, 5)
        self.image = pygame.transform.scale(pygame.image.load(f"coin1.png"), (30 + 5 * self.weight, 30 + 5 * self.weight))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -15)
        self.counter = 0

    def move(self):
        if self.active:
            self.rect.move_ip(0, 3)
            if self.rect.top > SCREEN_HEIGHT:
                self.active = False
            
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self, w):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), -50)
        self.active = False
        self.counter = w
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.active = True
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_UP] or pressed_keys[K_w]:
                self.rect.move_ip(0, -3)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN] or pressed_keys[K_s]:
                self.rect.move_ip(0, 3)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy(0)
E2 = Enemy(50)
E3 = Enemy(100)
C1 = Coin()
C2 = Coin()
C3 = Coin()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1, E2, E3)
coins = pygame.sprite.Group()
coins.add(C1, C2, C3)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, E2, E3, C1, C2, C3)
 
#Game Loop
while True:
    a += 2
    a = a % SCREEN_HEIGHT

    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #animating of backgroung
    DISPLAYSURF.blit(background, (0, a))
    DISPLAYSURF.blit(background, (0, a - SCREEN_HEIGHT))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        if entity.active:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))

          scores = font.render(str(SCORE), True, BLACK)
          DISPLAYSURF.blit(scores, (195 - 20 * len(str(SCORE)),325))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()

    #coin timer
    for coin in coins:
        if not coin.active:
            coin.counter += 1

        if coin.counter >= 60 * coin.weight:
            coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), -15)
            coin.active = True
            coin.counter = 0

        elif pygame.sprite.collide_rect(P1, coin):
            coin.rect.center = (random.randint(40, SCREEN_WIDTH-40), -15)
            coin.weight = random.randint(1, 5)
            coin.image = pygame.transform.scale(pygame.image.load(f"coin1.png"), (30 + 5 * coin.weight, 30 + 5 * coin.weight))
            coin.rect = coin.image.get_rect()
            SCORE += coin.weight
            SPEED = 4 + 0.5 * int(SCORE / 5)
            coin.active = False
    
    #enemies timer
    for enemy in enemies:
        if not enemy.active:
            enemy.counter += 1

        if enemy.counter >= 120:
            enemy.rect.center = (random.randint(40, SCREEN_WIDTH-40), -50)
            enemy.active = True
            enemy.counter = 0

    pygame.display.update()
    FramePerSec.tick(FPS)
