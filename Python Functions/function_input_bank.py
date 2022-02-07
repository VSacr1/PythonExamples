def deposit(total_amount, deposit_amount, customer_name):
    final_amount = total_amount + deposit_amount
    return f"The customer {customer_name} has a total bank amount of {final_amount}"

deposit_input = int(input("Please deposit an amount: "))

steves_bank_history = deposit(300, deposit_input, "Steve") 

print(steves_bank_history)

deposit_input_2 = int(input("Please deposit an amount: "))

steves_bank_history2 = deposit(800, deposit_input_2, "Steve")

print(steves_bank_history2)