import pygame, sys, time, os
from pygame.locals import *

pygame.init()

# Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("pyOS Paint")

clock = pygame.time.Clock()

# Background & canvas
bg_color = (0, 0, 0)
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(bg_color)

# Mode dan warna
mode = "paint"  # paint / eraser
colors = [(0,255,0), (0,0,255), (255,0,0)]  # hijau, biru, merah
color_index = 0
current_color = colors[color_index]

brush_size = 10
drawing = False
last_pos = None
fullscreen = False

# Folder script untuk SAVE
script_folder = os.path.dirname(os.path.abspath(__file__))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard shortcuts
        elif event.type == KEYDOWN:
            if event.key == K_p:
                mode = "paint"
                print("Mode: Paint")
            elif event.key == K_e:
                mode = "eraser"
                print("Mode: Eraser")
            elif event.key == K_c:
                color_index = (color_index + 1) % len(colors)
                current_color = colors[color_index]
                print(f"Color changed to {current_color}")
            elif event.key == K_b:
                canvas.fill(bg_color)
                print("Screen cleared")
            elif event.key == K_s:  # SAVE
                try:
                    filename = os.path.join(script_folder, f"paint_{int(time.time())}.png")
                    pygame.image.save(canvas, filename)
                    print(f"Image saved as {filename}")
                except Exception as e:
                    print(f"Error saat save: {e}")
            elif event.key == K_F11:  # fullscreen toggle
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0,0), FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
            elif event.key == K_F10:  # maximize windowed
                info = pygame.display.Info()
                screen = pygame.display.set_mode((info.current_w, info.current_h), RESIZABLE)
            elif event.key == K_F9:  # minimize
                pygame.display.iconify()

        # Mouse klik & drag
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        elif event.type == MOUSEMOTION:
            if drawing and last_pos:
                x, y = event.pos
                if mode == "paint":
                    pygame.draw.line(canvas, current_color, last_pos, (x, y), brush_size)
                elif mode == "eraser":
                    pygame.draw.line(canvas, bg_color, last_pos, (x, y), brush_size)
                last_pos = (x, y)

    # tampilkan canvas
    screen.blit(canvas, (0,0))
    pygame.display.flip()
    clock.tick(60)