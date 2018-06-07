list1=[1,2,3,4,5,6]
list2 = []
while (len(list1) > 1):
    print("List1 :", list1)
    # Find half the lengh of list1
    half_length = int(len(list1)/2)
    print("Half Length :", half_length)
    # Add half the values of n
    list2 = list2 + list1[0:half_length]
    print("List2 :", list2)
    # make list1 half the length of itself
    # then repeat the loop
    list1 = list1[0:half_length]
    
# Print the number of operations
print ("Number of operations: " , str(len(list2)))
