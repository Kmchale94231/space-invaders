import pygame
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True

        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width = alien.rect.width
        current_x = alien_width

        screen_width = self.screen.get_rect().width

        while current_x < (screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)

            current_x += 2 * alien_width

    def _update_screen(self):
        self.aliens.draw(self.screen)


    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")
            self._update_screen()
            pygame.display.flip()
            self.clock.tick(60)


        pygame.quit()


    