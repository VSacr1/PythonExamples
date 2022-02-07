class Pacman: 
    colour = "Yellow"

    hp = 100 

    soundeffect = "Waka Waka Waka Waka"

    def isDead(self): 
        hp = 0 
        if hp == 0:
            print("PacMan is dead wup wup wuuuuppp")

    
pacman = Pacman()
ms_pacman = Pacman()

print(pacman.soundeffect)
print(ms_pacman.soundeffect)

pacman.isDead()
