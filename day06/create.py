####################################################
# create and write to a file
# w: writable, r: read, a: append

myFile = open("test.txt", "r")
print(myFile.read())
myFile.close()


myFile = open("test_w.txt", "w")
myFile.write("This is a test")
myFile.write("But, without a newline")
myFile.write("\n Unless I purposely add it\n")
myFile.write('''Or 
with this 
other format\n''')

myList = ["This ", "is ", "a ", "test "]
myFile.writelines(myList)
# this method, delete the previous content
myFile.close()

# This method, add a new line
myFile = open("test_w.txt", "a")
myFile.write("Welcome !!!")
myFile.close()

