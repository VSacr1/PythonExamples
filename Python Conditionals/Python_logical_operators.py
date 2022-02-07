withdraw_amount = 110 
total_amount = 100
#Using and, can switch and with or. 
if withdraw_amount < total_amount and withdraw_amount > 0:
    new_total = total_amount - withdraw_amount 
    print(new_total)
else: 
    print("Invalid")


# _____________________________________________________
# Using nots to reverse the conditions
password = "password"

#This is now true 
if not password == "password378283892":
    print("Failed to make a deposit.")
else:
    print(f"Thank you for depositing £100!")


password1 = "Password123"
withdrawing = 1000
total_amount1 = 200

if not withdrawing < total_amount1 or password1 == "Password123":
    print(f"Depositing {withdrawing}")
else: 
    print("This is invalid")

age = int(input("Enter your age:"))

# Elif statements
if age >= 85: 
    print("You are above 85")
elif age >=50: 
    print("You are between 50 and 85")
elif age >= 20: 
    print("You are between 20 and 50")
else: 
    print("You are below 20")