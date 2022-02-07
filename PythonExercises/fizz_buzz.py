def fizzbuzz():

    for i in range(1, 20):
        if i % 3 == 0 and i % 5 == 0: 
            print("fizzbuzz")

        elif i % 3 == 0: 
            print("fizz")

        elif i % 5 == 0: 
            print("buzz") 
        
        else:
            print(i)
    # divisable by 3 = fizz 

    # divisable by 5 = buzz

    # if its divisable by 3 and 5 then its fizz buzz 

print(fizzbuzz())