line=input();
list1=line.split(" ")
list2=[]
for v in list1:
    if (type(v)== int):
        list2.append(int(v))
    else:
        list3=v.split()
        for c in list3:
            list2.append(c)
            
list2.insert(2,"Saduni")
print(list2)
