#!/usr/bin/env python
# coding: utf-8

# In[2]:


def nextprime(num):
    num +=1
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        return num
    
    
def primeproducer(N):
    num , counter = 1 ,1
    while count <=N:
        num = nextprime(num)
        yield num
        count +=1
        
N = int(input("How many prime number you want"))
l = [x for x in primeproducer(N)]
print(l)


# In[ ]:




