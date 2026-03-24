import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong!")

score_1 = 0
score_2 = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

p1 = pygame.Rect(50, 250, 20, 100)

ball = pygame.Rect(390, 290, 20, 20)

ball_speed_x = 5
ball_speed_y = 5

p2 = pygame.Rect(730, 250, 20, 100)

speed = 6
run = True
while run:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    #Player 1(WASD)
  
    if keys[pygame.K_w]:
        p1.y -= speed
    if keys[pygame.K_s]:
        p1.y += speed
        
    #Player 2 (ARROW)

    if keys[pygame.K_UP]:
        p2.y -= speed
    if keys[pygame.K_DOWN]:
        p2.y += speed
        
    
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    if ball.colliderect(p1) or ball.colliderect(p2):
        ball_speed_x *= -1
    
    #don't tell this secret!!!
    if keys[pygame.K_p]:
        ball_speed_x *= 1.2
        ball_speed_y *= 1.2

    if keys[pygame.K_9]:
        ball_speed_x *= 0.8
        ball_speed_y *= 0.8

   
    if ball.right < 0:
        score_2 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x = 5

    if ball.left > WIDTH:
        score_1 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x = -5



        
  
    
    p1.clamp_ip(screen.get_rect())
    p2.clamp_ip(screen.get_rect())
    
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (0, 255, 0), p1)
    pygame.draw.rect(screen, (0, 0, 255), p2)
    text = font.render(f"{score_1} : {score_2}", True, (255,255,255))
    screen.blit(text, (WIDTH//2 - 30, 20))
    pygame.display.update()
    
pygame.quit()