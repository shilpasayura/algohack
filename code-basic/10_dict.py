imgs=input()
imgx=imgs.split(" ")
xlist={}
for im in imgx:
    ix=im.split(".")
    ixx=int(ix[0].replace("IMG",""))
    
    xlist[ixx]= im
    
slist = sorted(xlist.keys())
newlist=[]
for imx in slist:
    newlist.append(xlist[imx])
    
print (newlist)

   
    
