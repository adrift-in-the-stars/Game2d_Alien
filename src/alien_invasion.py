import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from renderizador import Renderizador
from movimento_jogador import Movimento_jogador
from gerenciador_de_frota import Gerenciador_de_frota


class AlienInvasion:
    """Gerencia o jogo e seus comportamentos."""

    def __init__(self)->None:
        """Construtor da classe que inicializa o jogo e cria os recursos básicos"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Criando uma instância da classe Ship para representar a nave espacial
        self.ship = Ship(self.screen, self.settings)

        # Mudando a cor do plano de fundo em RGB
        self.bg_color = self.settings.bg_color

        self.bullets = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os projéteis disparados pela nave

        self.aliens = (
            pygame.sprite.Group()
        )  # Cria um grupo para armazenar os alienígenas presentes no jogo

    
    def fim_de_jogo(self)->None:
            if pygame.sprite.spritecollideany(
                self.ship, self.aliens
            ):  # Verifica se a nave colidiu com algum alienígena
                print(
                    "A nave foi atingida!"
                )  # Imprime uma mensagem no console indicando que a nave foi atingida
                sys.exit()  # Encerra o jogo


    def run_game(self)->None:
        """Cria um laço de repetição para a tela sempre ficar visível até
        que o usuário decida fechar a janela."""

        self.create_fleet()  # Cria a frota de alienígenas para ser desenhada na tela

        while True:
            #realiza logica de movimento da nave
            self.logica_de_movimento()

            # realiza logica de movimento dos projeteis
            self.logica_de_projeteis()

            # Verifica se algum projétil atingiu um alienígena
            # Em caso afirmativo, remove o projétil e o alienígena atingido
            self.abate()

            #movimenta os aliens
            self.movimentar_aliens()

            # Redesenha a tela a cada passagem pelo laço
            self.atualizar_tela()

            self.bullets.update()  # Atualiza a posição de cada projétil no grupo de projéteis

            self.aliens.update()  # Atualiza a posição de cada alienígena no grupo de alienígenas

            self.fim_de_jogo()#verifica se o o jogo deve terminar


if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
