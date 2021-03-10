r=1.2 #The rate of reproduction of a virus
I=84 #number of initial infected individuals

# j repersent the round number
# T is the total number of infected individuals
# b is newly infected individuals in round j
# a is the newly infected individuals in round j-1

#Initial situation
a=I
T=a

for j in range (1,6):
    b=a*r #the number of newly infected individuals equals to the number of newly infected individuals in last round
    T=T+b #add newly infected people into total number of infected individuals
    a=b #let people infected in this round become the "newly infected individuals in round j-1" in next round
print(T)
