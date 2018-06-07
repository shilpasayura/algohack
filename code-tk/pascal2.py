#Pascal Triangle 
# To build a Pascal Triangle we start with a “1” at the top.
# We then place numbers below each number in a triangular pattern:
# Each number is the result of adding the two numbers directly above it.



numberOfRows = 10

def formatNumber(number):
  if number<10:
    return "  "+str(number) + " "
  else:
    return " " + str(number) + " "

def printRow(row,rl):
    
    f="  " * (numberOfRows - rl)
    s=""
    for i in range(0, rl):
      s=s+ formatNumber(row[i])
    s=f+s
    return s
      

#6th Row
#print(row)
row=[1]
print(printRow(row,1))
row.append(1)
print(printRow(row,2))
for k in range(2, numberOfRows):
  temp=row[0]
  row.append(1)
  for i in range(0, len(row)-2):
      j=i+1
      temp2=row[j]
      row[j]=temp+row[j]
      temp=temp2
  print(printRow(row,k+1))


