import pygame

class Renderizador():

    def atualizar_tela(self)->None:
            #tela
            self.screen.fill(self.bg_color)

            # Redesenha a nave em sua posição atual
            self.ship.blitme()

            # alien.drawme() # Desenha os alienígenas presentes no grupo de alienígenas na tela
            self.aliens.draw(
                self.screen
            )  # Desenha os alienígenas presentes no grupo de alienígenas na tela

            # Atualiza a posição da nave com base na variável de controle
            self.ship.update()

            # Torna visível a tela mais recente
            pygame.display.flip()