import pygame
import sys

from bullet import Bullet

class Movimento_jogador():
    
    def logica_de_movimento(self)->None:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif (
                    event.type == pygame.KEYDOWN
                ):  # Detecta quando uma tecla é pressionada
                    if (
                        event.key == pygame.K_RIGHT
                    ):  # Verifica se a tecla pressionada é a seta para a direita
                        self.ship.moving_right = True
                    elif (
                        event.key == pygame.K_LEFT
                    ):  # Verifica se a tecla pressionada é a seta para a esquerda
                        self.ship.moving_left = True
                    elif (
                        event.key == pygame.K_SPACE
                    ):  # Verifica se a tecla pressionada é a barra de espaço
                        if (
                            len(self.bullets) < self.settings.bullet_allowed
                        ):  # Verifica se o número de projéteis na tela excede o limite permitido
                            new_bullet = Bullet(
                                self.screen, self.settings, self.ship
                            )  # Cria um novo projétil
                            # Aqui seria necessário adicionar o novo projétil a um grupo de projéteis para que ele possa ser atualizado e desenhado na tela
                            self.bullets.add(
                                new_bullet
                            )  # Adiciona o novo projétil ao grupo de projéteis

                elif event.type == pygame.KEYUP:  # Detecta quando uma tecla é liberada
                    if (
                        event.key == pygame.K_RIGHT
                    ):  # Verifica se a tecla liberada é a seta para a direita
                        self.ship.moving_right = False
                    elif (
                        event.key == pygame.K_LEFT
                    ):  # Verifica se a tecla liberada é a seta para a esquerda
                        self.ship.moving_left = False