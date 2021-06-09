class Ninja:

    def __init__( self , name='Player' ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def show_health(self):
        print(f"Health:  {self.health}")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self