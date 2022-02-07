from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self): 
        return "Squawk"
    
    def reproduce(self): 
        self.babies +=1 

    @abstractmethod
    def eat(self):
        pass 

    extinct = False 


class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self): 
        return "Peck Peck!"


class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

owlet = Owl() 
owl2 = Owl()

print(owlet.fly)
print(owl2.babies) #0
owl2.reproduce()
print(owl2.babies) #6
owl2.reproduce()
print(owl2.babies) #12

dodo1 = Dodo()

dodo1.extinct = False
dodo1.reproduce()
print(dodo1.babies)
