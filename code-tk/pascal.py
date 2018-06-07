#Pascal Triangle 
# To build a Pascal Triangle we start with a “1” at the top.
# We then place numbers below each number in a triangular pattern:
# Each number is the result of adding the two numbers directly above it.



numberOfRows = 7

def formatNumber(number):
  if number<10:
    return "  "+str(number) + " "
  else:
    return " " + str(number) + " "

#First Row
row = [1]
print("  " * 7 + formatNumber(row[0]))

#Second Row
row.append(1)
print("  " * 6 + formatNumber(row[0]) + formatNumber(row[1]))

#third Row
row.append(1)
row[1]=row[0]+row[1]
print(row)

#forth Row
row.append(1)
row[2]=row[1]+row[2]
print(row)
