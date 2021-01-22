import os
import pygame

WIDTH = 920
HEIGHT = 780
FPS = 30

BLACK = (0, 0, 0)


class Entity(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        hourglass_img = pygame.image.load(os.path.join(img_folder, 'hourglass.png')).convert()

        self.image = hourglass_img

        self.orig_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def update(self):
        self.angle -= 2
        self.rotate()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group(Entity((WIDTH/2, HEIGHT/2)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
