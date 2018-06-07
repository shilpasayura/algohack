list1= [1, 5, 6, 2, 4, 3]
op=0
for i in range(len(list1)):
  key = list1[i] # first item
  j = i-1
  while(j>=0 and key < list1[j]):
    list1[j+1] = list1[j]
    j=j-1
    op=op+1
  list1[j+1] = key
print(op,list1)
