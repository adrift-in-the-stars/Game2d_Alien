import pygame
from bullet import Bullet

class BulletManager:
    """Cria atualiza e desenha projeteis"""
    def __init__(self, screen, settings, ship)->None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullet = pygame.spriteGroup()

    def _fire_bullet(self)->None:
        """Dispara um projetel se o limite não estiver atingido"""
        if(len(self.bullets) < self.settings.bullet_allowed):
            new_bullet = Bullet(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def _update_bullets(self, aliens)->None:
        """Atualiza a posição dos projeteis e eliminaprojeteis inuteis"""
        self.bullets.update()
        self._remove_offscreen_bullets()
        self._check_bullet_alien_collisions(aliens)

    def _remove_offscreen_bullets(self)->None:
        """Destroi projeteis fora da tela"""
        for bullet in self.bullets.copy():
            if(bullet.rect.botton <= 0):
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self, aliens)->None:
        """Verifica colisões entre projeteis e alienigenas"""
        pygame.sprite.groupcollide(self.bullets, aliens, True, True)