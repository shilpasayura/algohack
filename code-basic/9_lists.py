line=input();
def isInt(v):
    try:     i = int(v)
    except:  return False
    return True

line=input();
list1=line.split(" ")
list2=[]
for v in list1:
    if isInt(v):
        list2.append(int(v))
    else:
        list3=list(v)
        for c in list3:
            list2.append(c)
            
list2.insert(2,"Sanduni")
print(list2)
