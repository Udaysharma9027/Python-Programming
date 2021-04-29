#!/usr/bin/env python
# coding: utf-8

# In[2]:


f = (lambda n: n*f(n-1) if n>0 else 1)
print(f)


# In[ ]:




