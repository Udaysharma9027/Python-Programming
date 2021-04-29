#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input("Enter  a number"))
if n <2:
    print("Not a prime number")
else:
    for i in range (2 , n):
        if n%i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


# In[ ]:





# In[ ]:




