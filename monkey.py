import numpy as np

d=np.zeros((101),dtype=int)


i=1

while (i<=100):
    for j in range(101):
        if((j%i)!=0):
            continue
        else:
            if(d[j]!=1):
                d[j]=1
            else:
                d[j]=0
    i+=1


count=0
for i in range(101):
    if(d[i]==1):
        count+=1
        

print(d)

print(count)

