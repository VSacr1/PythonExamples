bank_total = 300 
deposit_money = 40
withdraw_money = 320

# if deposit money is greater than 0
if deposit_money > 0: 
    new_total = bank_total + deposit_money
    print(new_total)

else: 
    print("Invalid deposit total")

# If withdraw_money is less than or equal to bank_total
if withdraw_money <= bank_total:
    # if withdraw_money is greater than or equal to 0 
    if withdraw_money >= 0: 
        new_total = bank_total - withdraw_money
        print(new_total)
    else: 
        print("invalid withdraw amount")

else: 
    print("Invalid withdraw amount, not enough in the bank")