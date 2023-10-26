import pygame
pygame.init()
import random
import math

w = pygame.display.set_mode([800, 600])

#Background
background = pygame.image.load("background.png")

#Player
player = pygame.image.load("spaceship.png")
px = 365
px_change = 0
py = 480 



#enemy

enemy = pygame.image.load("enemy.png")
ex = random.randint(0,736)
ex_change = 2
ey_change = 50
ey = random.randint(50,150)




#bullet
bullet = pygame.image.load("bullet.png")
bx = 0
by = 480
bx_change = 0
by_change = 10
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10

def show_score(x,y):
  score = font.render("Score: " + str(score_value),True,(255,255,255))
  w.blit(score,(x,y))

#Define the creation of player
def playerload (x,y):
  w.blit(player,(x,y))

#Define the creation of enemy
def enemyload (x,y):
  w.blit(enemy,(x,y))
#fire bullet
def fire_bullet(x,y):
  global bullet_state
  bullet_state = "fire"
  w.blit(bullet,(x+ 16,y+ 10))

def isCollision(ex,ey,bx,by):
  distance = math.sqrt(math.pow(ex-bx,2) + math.pow(ey-by,2))
  if distance < 27:
    return True
  else:
    return False

run = True
while run:
  #Fill the background every iteration
  w.fill((0, 0, 0))
  w.blit(background,(0,0))
  

  

  #Make the player move
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        px_change = -1

      if event.key == pygame.K_RIGHT:
        px_change = 1

      if event.key == pygame.K_SPACE:
        if bullet_state == "ready":
          bx = px
          fire_bullet(bx,by)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        px_change = 0
  #COmponents movements
  px += px_change
  
  

  # Border the player
  if px >= 736:
    px = 736
  if px <= 0:
    px = 0

  
  ex += ex_change
  #Border the enemy
  if ex >= 736:
    ex_change = -2
    ey += ey_change
  elif ex <= 0:
    ex_change = 2
    ey += ey_change
  
  #Detect collision
  collision = isCollision(ex,ey,bx,by)
  if collision:
    by = 480
    bullet_state = "ready"
    score_value += 10
    ex = random.randint(0,735)
    ey = random.randint(50,150)
    
  enemyload(ex,ey)



  #fire the bullet
  if bullet_state == "fire":
    fire_bullet(bx,by)
    by -= by_change
  
  #Retrive the bullet
  if by < 100:
    by = 480
    bullet_state = "ready"
  
  
  
    
  #Deploy components
  playerload(px,py)
  

  #Update and flip the display
  show_score(textx,texty)
  pygame.display.update()
  pygame.display.flip()

