
fo = open("file.txt", "r+")
str = fo.read(5); # read 5 characters
print ("String is : ", str)
# Check current position
position = fo.tell();
print ("Current position : ", position)

# Reposition pointer at the beginning again
position = fo.seek(0, 0)
position = fo.tell();
print ("Current position : ", position)
str = fo.read(5)
print ("Again reading String : ", str)
str = fo.read(5)
position = fo.tell();
print ("Current position : ", position)
position = fo.seek(0, 1)
str = fo.read(4)
print ("String : ", str)
position = fo.tell();
print ("Current position : ", position)
fo.close()
