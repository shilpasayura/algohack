def qsort(L1):
    smaller = []
    equal = []
    bigger = []
    if len(L1) == 0:
        return []
    pivot = L1[0]
    
    for x in L1:
        if (x < pivot):
            smaller.append(x)
        elif (x > pivot):
            bigger.append(x)
        else :
            equal.append(x)
            
        a1=qsort(smaller)
        a2=qsort(bigger)
        L1=a1+equal+ a2
    return L1
    
L1=[7,6,18,12,0,4,3,21]
L2=qsort(L1)
print(L1,L2)

    
