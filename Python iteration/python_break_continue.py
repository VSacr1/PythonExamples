for i in range(10):
    #print(i)
    
    if i > 7: 
        break

for i in range(10):
    if i == 5: 
        continue
    #print(i)


maths = 0

while maths == 0: 
    maths = int(input("please input maths grade"))

    if maths < 0 or maths > 100: 
        continue

    else: 
        print(maths)

    