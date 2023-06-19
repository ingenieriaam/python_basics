####################################################
# Input and Output files

myFile = open("test.txt")
print(myFile)

print(myFile.read())
myFile.close()

# for each line
myFile = open("test.txt")
print(myFile.readline())
print(myFile.readline())
print(myFile.readline().upper())
myFile.close()

myFile = open("test.txt")
for l in myFile:
    print(l)
myFile.close()

myFile = open("test.txt")
all_lines = myFile.readlines()
print(all_lines)
all_lines.pop(1)
print(all_lines)

# IMPORTANT: close the file
myFile.close()
