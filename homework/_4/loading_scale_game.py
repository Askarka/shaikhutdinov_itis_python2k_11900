# Pygame шаблон - скелет для нового проекта Pygame
import pygame

# window parameters
WIDTH = 860
HEIGHT = 480
FPS = 30
RECT_WIDTH = 310
RECT_HEIGHT = 75

# colours
BACKGROUND_COLOUR = (87, 101, 116)
BACK_RECT_COLOR = (200, 214, 229)
FRONT_RECT_COLOR = (29, 209, 161)
# making game and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loading Scale game")
clock = pygame.time.Clock()

completeness_ratio = 0

# game cycle
running = True
while running:
    clock.tick(FPS)
    # actions
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # chek for keystrokes
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if completeness_ratio > 0:
                    completeness_ratio -= 5
            elif event.key == pygame.K_RIGHT:
                if completeness_ratio < 100:
                    completeness_ratio += 5

    # Updating

    # Rendering
    screen.fill(BACKGROUND_COLOUR)
    pygame.draw.rect(screen, BACK_RECT_COLOR,
                     ((WIDTH - RECT_WIDTH) / 2, (HEIGHT - RECT_HEIGHT) / 2, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(screen, FRONT_RECT_COLOR,
                     ((WIDTH - RECT_WIDTH) / 2, (HEIGHT - RECT_HEIGHT) / 2, RECT_WIDTH*completeness_ratio/100, RECT_HEIGHT))

    # showing changes
    pygame.display.flip()

pygame.quit()
