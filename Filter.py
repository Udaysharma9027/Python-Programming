#!/usr/bin/env python
# coding: utf-8

# In[7]:


my_list = ["uday" , "keshav" , "sumit"]
my_filter = list(filter(lambda x : len(x) >=2  , my_list))
print(my_filter)


# In[9]:


my_list = [52 , 65 , 69 , 86 , 100 , 86]
my_filter1 = list(filter(lambda x :x<=100 , my_list))
print("Your answer is {}" . format(my_filter1))


# In[ ]:




