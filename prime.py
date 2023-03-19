import math as m

pr=[]

n=int (input('enter the range'))

flag=0
for i in range(2,n):
     y = m.sqrt(i)
     j=2
     while(j<=y):
          if(i%j==0):
             flag=1
             break
          else:
            flag=0
          j+=1
     if(flag==0):
        pr.append(i)
        
print(pr)

""" 
TO CALCULATE THE NUMBER OF TIME A PRIME
COME IN A NUMBER FACTORIAL

n=int(input('enter the range'))

p=int(input('enter the prime'))
z=0
for i in range (1,10):
    x=m.pow(p,i)
    z+=m.floor(n/x)
   

print(z)


for k in range(1,10):
    l=int(m.sqrt(k))
    print(l,end='\n')
"""
