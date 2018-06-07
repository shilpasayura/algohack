import pdb
list1 = [5,4,3,1,6,8,7,0,2] # not sorted
list1.sort() 
print (list1)
n=len(list1)
for i in range(n):
    for j in range(i+1, n):
        print ("Checking index", i,   j )
        if(list1[i] > list1[j]):
            print ("swaping ", list1[i],  list1[j] )
            temp=list1[i]
            list1[i] = list1[j]
            list1[j]=temp
print (list1)
