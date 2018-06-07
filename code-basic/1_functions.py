arr =[float(x) for x in input().split()]
arr.sort();
n=len(arr)
print(arr[n-1])
for i in range(n):
    arr[i]=round(arr[i])
    #print (arr[i])
arr.reverse();
print (arr)
