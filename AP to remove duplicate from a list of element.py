#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = []
n = int(input("How many name u want to enter"))
for i in range(n) :
    print(i+1 , "Enter name")
    name.append(input())
s = set(name)
for x in s:
    print(x)


# In[ ]:




