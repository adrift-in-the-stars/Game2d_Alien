from alien import Alien

class FastAlien(Alien):
    """Um alien mais rapido"""

    def update(self)->None:
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x