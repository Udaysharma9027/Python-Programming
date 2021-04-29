#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
-- Creating a online bank
-- User can new account that include . Account type (current , saving , etc) , name of account holder , account balance etc
-- user can withdraw money , deposit or check balance
"""


# In[7]:


class bank:
    def __init__(self ,Account_type , name , Amount):
        self.Account_type = Account_type
        self.name = name
        self.Amount = Amount
    def check_balance(self):
        print("Your balance is {}".format(self.Amount))
    def Deposit(self , deposit_amount):
        self.Amount+=deposit_amount
    def With_draw(self , with_draw):
        self.Amount += with_draw
        
        
Jhon_Account = bank("Current" , "Jhon" , 50000 )
Sumit_Account = bank("Saving" , "Sumit" , 20000 )
Mona_Account = bank("Current" , "Mona" , 80000 )
Pinku_Account = bank("Savinf" , "Pinku" , 70000 )
Pankaj_Account = bank("Current" , "Pankaj" , 980000)


Pankaj_Account.With_draw(800000000)
Pankaj_Account.check_balance()



# In[ ]:





# In[ ]:




