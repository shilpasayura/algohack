N=int(input())
S=format(N, "04b")
SD=int(S)
S1='{0:#<54b}'.format(N)
S2='{:*<8d}'. format(SD)
S3='{:.6f}'. format(N)

S4='{:.6e}'. format(float(S3))

#S1="#" + S1
S3=S3+"$"
S4="^"+S4+"^^"

print(S1)
print(S2)
print(S3)
print(S4)
