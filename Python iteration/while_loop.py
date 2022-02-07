number = 0 

while number <= 2: 
    print(number)
    number += 1


my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:
    print(fruit.upper())

names = ["Victoria", "Ben", "Harry", "Reece"]

for name in names: 
    print(name.lower())


#grade1 = int(input("Please enter a grade: "))

#while grade1 < 0 or grade1 > 100:
 #   grade1 = int(input("Please try again!"))

#if grade1 > 80: 
 #   print("You got an A") 


grades = [30,50, 60, 90, 20, 10, 40]

for grade in grades:
    if grade >= 50: 
        print("You pass! Hurray")
    else: 
        print("You Failed")
