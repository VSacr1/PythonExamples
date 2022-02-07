from tkinter import Pack

class Pacman: 
    def __init__(self, colour, hit_Points, soundeffect):
            self.colour = colour 
            self.hit_points = hit_Points
            self.soundeffect = soundeffect 

    def isDead(self):
        return "Pacman is dead. oh no!"

pacman = Pacman("Yellow", 100, "Waka Waka Waka")
ms_pacman = Pacman("Blue", 110, "Eat, Eat, Eat")
pacman_jr = Pacman("Red", 60, "Waka, Eat, Waka, Eat")

print(pacman.colour)
print(pacman.soundeffect)
print(pacman.isDead())
print(pacman_jr.soundeffect)