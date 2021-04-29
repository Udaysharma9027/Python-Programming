#!/usr/bin/env python
# coding: utf-8

# In[ ]:


for i in range (1001):
    num = i
    result = 0
    n = len(str(i))
    while(i!=0):
        digits = i%10
        result = result + digits **n
        i = i//10
    if num == result:
        print(num)


# In[ ]:




