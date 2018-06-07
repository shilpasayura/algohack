def mergesort(list): 
    mid = len(list)//2 
    left, right = list[:mid], list[mid:] 
    if len(left) > 1:
        left = mergesort(left) 
    if len(right) > 1:
        right = mergesort(right) 
    res = [] 
    while left and right: 
        if left[-1] >= right[-1]: 
            res.append(left.pop()) 
        else: 
            res.append(right.pop()) 
    res.reverse()
    if (left):
        list=left+res
    else:
        list=right+res
    return list

list=[4,7,2,6,12,9,5]
list =mergesort(list)
print(list)
