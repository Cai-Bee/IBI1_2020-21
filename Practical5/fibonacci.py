a=1
b=1
c=2
#a,b is the two number before c
for j in range(3,14): #j is the position of number c
#c will be the sum of the two number before it
    c=a+b
    a=b
    b=c
    print("count",j, c)
