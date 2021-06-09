class Pirate:

    def __init__( self , name='Player' ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def show_health(self):
        print(f"Health:  {self.health}")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

    def buff(self):
        self.strength += 30
        return self

    def restore_all(self):
        self.health = 100