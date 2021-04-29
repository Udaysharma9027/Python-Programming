#!/usr/bin/env python
# coding: utf-8

# In[1]:


def nextprime(n):
    while True:
        n+=1
        for i in range(2 ,n):
            if n%i == 0:
                break
        else:
            return n
        
nextprime(455)
        


# In[ ]:





# In[ ]:




