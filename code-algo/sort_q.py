def quicksort(L1):
    if (len(L1)==0):
        return []

    pivots = [x for x in L1 if x == L1[0]]
    lesser = quicksort([x for x in L1 if x < L1[0]])
    greater = quicksort([x for x in L1 if x > L1[0]])

    return lesser + pivots + greater

list1= []
op=0
list2=quicksort(list1)
print(list2)
