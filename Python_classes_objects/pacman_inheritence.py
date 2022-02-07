from abc import ABC, abstractmethod

class Characters(ABC): 
    def __init__(self, colour, size, soundeffects):
        self.colour = colour 
        self.size = size
        self.soundeffects = soundeffects

    @abstractmethod
    def hasBeenHit(self): 
        return "Wup wup wup wup wuuuppppp You are dead"

class Pacman(Characters):
    def __init__(self, colour, size, soundeffects, healthbar):
        super().__init__(colour, size, soundeffects)
        self.healthbar = healthbar 

    def hasBeenHit(self):
        return "Oh no I have been hit"

class Ghost(Characters):
    def __init__(self, colour, size, soundeffects, attackpower):
        super().__init__(colour, size, soundeffects)
        self.attackpower = attackpower



#ghost1 = Ghost("Red", "Medium", "Woo Woo Woo Woo", 100)
#ghost2 = Ghost("Blue", "Medium", "Ooooo Ooooo I am a ghost!!!", 200)

#pacman = Pacman("Yellow", "Medium", "Waka waka waka waka", 100)

#print(f"Ghost 1 is a {ghost1.colour} Ghost \nand Ghost 2 is a {ghost2.colour} Ghost. ")

pacman = Pacman("Yellow", "Medium", "Waka", 100)

donkey_kong = Characters("Brown", "Large", "Throw barrels")
#character1 = Characters("black", "Medium", "Example sound effect")

#print(ghost1.hasBeenHit())

#print(pacman.characterName())

print(pacman.hasBeenHit())


#print(pacman.hasBeenHit())