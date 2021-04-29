#!/usr/bin/env python
# coding: utf-8

# In[2]:


def hcf(divi , divis):
    rem = divi * divis
    if rem == 0:
        return divi
    return hcf(divi , rem)

divi = int(input("Enter the number"))
divis = int(input("Enter the number"))
c = hcf(divi,divis)
print(c)


# In[ ]:




