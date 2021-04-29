#!/usr/bin/env python
# coding: utf-8

# In[2]:


list_one = [8,9,9,6,4]
list_two = list(map(lambda x:x*9 , list_one))
print("your answer is{}".format(list_two))


# In[5]:


tuple_one = (89 , 96 , 86 , 86, 45)
tuple_two = tuple(map(lambda x:x*1000 , tuple_one))
print("Your answer is {}".format(tuple_two))


# In[7]:


list_one = [15 , 69 , 56 , 45]
list_two = [56 , 86 , 96 , 86]
list_three = list(map(lambda x , y: x+y , list_one , list_two))
print("your addition is {}".format(list_three))


# In[ ]:




