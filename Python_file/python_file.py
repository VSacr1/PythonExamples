file = open("example.txt", "r")

# readline() - reads the current line and then moves on to the next 
#print(file.readline()) # 1st line 
#file.readline() # 2nd line but not print
#print(file.readline()) # 3rd line 

# read() - Reads from the current line to the end of the file. 
#print(file.read()) # 4th line down to the end of the document

# Seek find the index and takes you to this index. Useful for navigating through documents
# EG 0 = L
# 1 = o  

#read all lines
all_lines = file.read()
print(all_lines)
# print line at index 1 (2nd line)
#print(all_lines[1])
#file.seek(0) 

#print(file.readline())

#read() - Which reads from the current line to the end of the file. 

file.close()

file = open("example.txt", "w")

file.write(all_lines)
#for n in range(1, 11):
#    newline = "This is line " + str(n) + "\n"
#    file.write(newline)

new_text = "This is line 11"
file.write(new_text + "\n")
file.close()

# I dont have to write file.close. 
# Automatically closes the file. 
with open("filename.txt", "w") as file:
    for n in range(1,11):
        newline = "This is line" + str(n) + "\n"
        file.write(newline)