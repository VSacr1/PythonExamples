# This code doesn't work please fix my code!!!! 
ISBN = input("Please enter the 12 digit numbers")

counter = 0 
while len(ISBN)!= 12:
    print("Please enter 12 digits")
    continue 

isbn_list = []
if len(ISBN) == 12:
    for i in ISBN: 
        isbn_list.append(i)
        if int(i) % 2 == 0: 
            new_counter = counter + i
            print(counter)

        else: 
            # if index is odd
            new_counter = new_counter + (i * 3)
