r=1.2 #The rate of reproduction of a virus
I=84 #number of initial infected individuals

T = I
for i in range(1,6):
    T += T*r

T = int(T)
print("The r rate is "+str(r)+". The total number of individuals infected after 5 generations is "+str(T))
