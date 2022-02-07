cool_cows = ["Winnie the moo", "Moolan", "Milkshake", "Mooana"]

print(cool_cows[3])

print(cool_cows[0:3])

print(cool_cows[0:2])

print(cool_cows[-1])

print(cool_cows[2:])

cool_cows[1] = "Aladdin but a cow"

del cool_cows[0]

print(cool_cows)

del cool_cows[0]
print(cool_cows)
print(cool_cows[0])

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals[1][1])
print(cool_animals[2][1:])

my_fruit = ['Apple', 'Avacado', 'Banana', 'Orange', 'Passionfruit', 'apples', 'pears', 'banana', 'kiwi']
my_fruit.sort()
print(my_fruit)

print(", ".join(my_fruit))

my_fruit.pop(0)
print(my_fruit)