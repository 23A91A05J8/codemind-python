a=int(input())
b=int(input())
c=int(input())
res=(2*a*b*c*512)/1024
c = '{:.0f}'.format(res)
print(str(c)+" "+"KB")