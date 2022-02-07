# Python Introduction 
print("Hello world!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(type(age))

print(name)
print(age)

# BIDMAS
# 1st 2 x 20 
# 2nd Division
# 3rd Addition
# 4th Subtraction
x = 10 / (2 * 20) + 7 - 2
print(x)

# 1st Division
# 2nd Multiplication
# 3rd Addition
# 4th Subtraction
y = 10 / 2 * 20 + 7 - 2
print(y)

# String Manipulation
hello = "Hello World" 

#Lower case
print(hello.lower())

#Upper case
print(hello.upper())

# Replace
hellov2 = hello.replace("World", "Everybody")

print(hellov2)

print(hellov2.upper())

#Split 
print(hello.split())

# Join
list1 = ["Hello", "World"]

print(" ".join(list1))

# Count
print(hello.count("l"))

# Is there a digit in the text
print(hello.isdigit())

x = "Hello"

age = 28

# Concatinating
print("Victoria" + " " + "Trainer")
# Not Concatinating -> print("Victoria", "Trainer")
print("Victoria" + " " + str(age+10))

# f strings
print(f"This is my age {age}")

# Escape Characters
print('Hello this is \"Victoria\"')

print(f"Person 1: \t {x}, how are you? \nPerson 2: \t Good thanks! \U0001F604")

# Integers and Floats
print(int(3.6))

print(float(3))
#Rounding a number up or down
print(round(3.5739375))

# Booleans
print(4 < 20)

print(4 > 20)