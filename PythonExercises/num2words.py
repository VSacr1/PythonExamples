from unicodedata import digit


digits = {1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five"}
tens = {10 : "ten", 20: "twenty"}
user_input = int(input("Please put a number between 1 and three: "))
lists = []

for i in digits.values():
    lists.append(i) 
    #1print(lists)

if user_input == 1: 
    print(lists[0])
elif user_input == 2: 
    print(lists[1])
elif user_input == 3: 
    print(lists[2])

new_list = []

for i in str(user_input): 
    new_list.append(i)
    print(new_list)

tens_list = [] 

for j in tens.values(): 
    tens_list.append(j)

if int(new_list[1]) > 0 and int(new_list[0]) > 1: 
    if int(new_list[0]) == 2: 
        tens_value = f"{tens_list[1]}"
    if int(new_list[1]) == 1: 
        digitexample = f"{lists[0]}"

print(tens_value + digitexample)