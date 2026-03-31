import pygame
import sys
from alien import Alien

class FleetManager:
    """Gerencia a frota de aliens"""
    def __init__(self, screen, settings, ship)->None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullet = pygame.spriteGroup()

    def _create_alien(self, alien_number: int, row_number: int, alien_width: int, alien_height: int)->None:
        """Cria um alien e o coloca na linha"""
        alien = self.alien_class(self.screen, self.settings)
        alien.width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien_height = alien.rect.heigth
        alien.y = alien_height + 2 * alien_height * row_number
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def create_fleet(self)->None:
        """Cria uma frota de alienígenas."""
        # Cria um alienígena e calcula o número de alienígenas em uma linha
        # O espaçamento entre os alienígenas é igual a um alienígena
        alien = self.alien_class(self.screen, self.settings)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect_width
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)

        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Cria a primeira linha de aliens
            for alien_number in range(number_aliens_x):
                # Cria o alien e coloca na linha
                self._create_alien(alien_number, row_number, alien_width, alien_height)

    def _update_aliens(self)->None:
        self._check_fleet_edges()
        self.aliens.update()
        self._check_ship_collision()

    def _check_fleet_edges(self)->None:
        """Responde se um alien alcançar a borda"""
        for alien in self.aliens.sprites():
            if (alien.check_edges()):
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self)->None:
        """Desce a forta e muda a direção"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_ship_collision(self)->None:
        """Verifica colosão da nave com um alien"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("A nave foi atingida!")
            sys.exit()