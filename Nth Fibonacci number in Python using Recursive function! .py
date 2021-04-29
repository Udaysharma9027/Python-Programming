#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter the number"))
def fib(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fib(x-1)*fib(x-2)

print("The" , n ,"Fibnonic Series" , fib(n))


# In[ ]:




