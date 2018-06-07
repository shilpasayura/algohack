list=[7,6,18,12,0,4,3,21]
N=len(list)
for i in range(1,N):
    x=list[i]
    j=i
    while(j>0 and list[j-1]>x):
        list[j]=list[j-1]
        j=j-1
        
    list[j]=x
    
print(list)
