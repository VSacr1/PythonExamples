cool_cows = "Winnie the Moo", "Moolan", "Milkshake", "Mooana"

cool_cows_string = "Winnie the Moo, Moolan, Milkshake, Mooana"

stringexample1 = "This_is_a_string" 

#cool_cows_string[1]="a"

farm = "Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850

farm_name, cool_cows, farm_size = farm 

#print(farm_name)

noises = { "cow" : "moo", "sheep" : "baa"}

noises1 = {"cow" : ["Winnie the moo", "moolan"]}

noises["chicken"] = "cluck"
noises["sheep"] = "meh"
noises["rooster"] = "crow"

print(noises1["cow"])

#print(noises)

#tupleexample = tuple(noises.keys())
#print(tupleexample)

#print(tuple(noises.values()))

#winniemoo, barbra, chuck, clucker = tupleexample

#print(winniemoo)

#print(noises.keys())

#print("moo" in noises.values())

my_items = ["Apple", "Banana", "Apple", "Banana", "Orange"]

#print(set(my_items))

new_set = {1,2,3,4,5,6,7,8,9,10}
new_set1 = [1,2,3,4,5,4,7,5,6,7,8,9,10]
print(set(new_set1))

new_set.add(11)

new_set.discard(3)
new_set.discard(3)

#print(new_set)

set1 = {1, 2, 3} 
set2 = {1, 2, 3}

result = set1 < set2 
print(result)