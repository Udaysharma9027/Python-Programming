#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Animals:
    def __init__(self , name , colour , noise):
        self.name = name
        self.colour = colour
        self.noise = noise
        
    def describe(self):
        print("The {} is {} and it noise is {}".format(self.name , self.colour , self.noise))
    
owl = Animals("Owl" , "Brown" , "Twit tawooo")
Dog = Animals("Dog" , "Black" , "Woooo")

owl.colour
Dog.describe()


# In[ ]:




