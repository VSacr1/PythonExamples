hello = "Hello Everyone, this is Victoria!"
lists = []

# This picks up items from the string and puts every word into a list.
#for char in hello.split():
    #lists.append(char)
    #print(lists)
    #print(char)

#print(lists)
#print(lists[2])

new_dictionary = {"key1" : "Value1", "key2" : "Value2", "key3": "Value3"}

for items in new_dictionary.items():
    print(items)

result = []

for x in range(5): 
    result.append(x)

print(result)

print([x for x in range(5)])