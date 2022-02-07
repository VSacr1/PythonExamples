def greet(firstname, lastname):
     print(f"Hello {firstname} {lastname}")


greet("Victoria", "Smith")
greet("Greg", "Example")
greet("Steve", "Rogers")

# This function takes in firstname and lastname as arguements
# This returns me "Hello {firstname} {lastname}"
def greet(firstname, lastname):
    return f"Hello {firstname} {lastname}"


first_name = input("What is my first_name")
last_name = input("What is my last name")

steve_rodgers = greet(first_name, last_name)

victoria_smith = greet("Victoria", "Smith")



lists = []

lists.append(steve_rodgers)

print(lists)