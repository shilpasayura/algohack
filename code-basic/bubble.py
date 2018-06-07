list1=[1,2,6,12]
iteration=0

print ("iteration", iteration, list1)
for i in range(len(list1)):
    for j in range(len(list1)-1-i):
        iteration=iteration+1
        if list1[j]> list1[j+1]:
            temp=list1[j]
            list1[j] = list1[j+1]
            list1[j+1]=temp # Swap!

        print ("iteration", iteration, list1)
print(list1)
