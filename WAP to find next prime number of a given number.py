#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter a number"))
while True:
    n+=1
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print(n)
        break


# In[ ]:




