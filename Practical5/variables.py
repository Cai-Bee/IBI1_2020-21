a=200402
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)

#compare between d and e
if d>e:
    print("d>e")
elif d<e:
    d<e
else:
    print("d=e")

X=True
Y=False

Z = (X and not Y) or (Y and not X)
W = X!=Y
#W == Z for all 4 combinations of X and Y (TRUE/FALSE)
bool = [True, False]
for X in bool:
    for Y in bool:
        p = Z==W
        print("When X = "+str(X)+", Y = "+str(Y)+"   Z==W is "+str(p))
