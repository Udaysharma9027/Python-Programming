#!/usr/bin/env python
# coding: utf-8

# In[6]:


class person :
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def age_report(self):
        print("Hii {} your age is {}".format(self.name, self.age))
    def age_plush(self):
        self.age+=1
        print("Hii {} your age increase by {}".format(self.name , self.age))
        
person_one = person("UdaySharma" , 20)
person_two = person("KeshavArya" , 21)

person_two.age_plush()


# In[10]:


class Warrior:
    def __init__(self , name , strength , health):
        self.name = name
        self.strength = strength 
        self.health = health
    def report(self):
        print("Hii {} . Your strength is {} and your health is{}".format(self.name , self.strength , self.health))
    def health(self):
        self.health += 1
        print("Hii {} .your strength is {} and your health is increased by {} ".format(self.name , self.strength , self.health))
    def damge (self):
        self.health-=1
        print("Hii {} .your strength is {} and your health is damged by {}".format(self.name , self.strength , self.health))
    def workout(self):
        self.strength+=1
        print("Hii {} . your strength is incresed by {} and your health is {}".format(self.name , self.strength , self.health))
        
person_one = Warrior("Sumit" , 10 , 100)
person_two = Warrior("Prakash" , 15 , 90)

person_one.damge()


# In[ ]:





# In[ ]:




