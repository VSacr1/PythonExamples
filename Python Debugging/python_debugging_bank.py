import pdb 

#Start debugging
pdb.set_trace()

def deposit(total_amount, deposit_amount, customer_name):
    final_amount = total_amount + deposit_amount
    return f"The customer {customer_name} has a total bank amount of {final_amount}"

def withdrawal(total_amount, deposit_amount, customer_name):
    final_amount = total_amount + deposit_amount
    return f"The customer {customer_name} has a total bank amount of {final_amount}"

print(deposit(300, 200, "Steve"))

print(withdrawal(300,400,"Steve"))