def sort(array):
    less = []
    equal = []
    greater = []
   
    if len(array) == 0:
        return []
    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
       
        if x > pivot:
            greater.append(x)
            
    array=sort(less)+ equal +sort(greater)
    return array

L1=[7,6,18,12,0,4,3,21]
L2=sort(L1)
print(L1,L2)

    
