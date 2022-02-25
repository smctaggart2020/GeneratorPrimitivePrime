#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Consider all the possible sets of two square roots s, t of 1 (mod 77) where s ≢ t (mod 77) 
Note: since there are 4 different roots, there are 6 combinations of distinct roots. 
or all possible combinations of distinct roots s & t, compute gcd(s + t, 77). 
Which combinations give you a single prime factor of 77?"""

import math
x=0 #start value 
l1=[]
while x<=76:  
    a=x*x%7  
    b=x*x%11 
    if a==b==1:
        print(f'{x} (mod 77) = < {a} (mod 7) {b} (mod 11) >')
        l1.append(x)    
    x+=1
d1={}
for i in l1:
    for j in range(1,len(l1)):
        if i < l1[j]:
            d1[(i,l1[j])] = math.gcd(i+l1[j],77)
        elif i > l1[j]:
             d1[(l1[j],i)] = math.gcd(i+l1[j],77)
print(d1)
for key in d1:
    print((d1[key]))


# In[ ]:




