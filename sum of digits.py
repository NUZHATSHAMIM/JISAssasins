#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


#write a program to calculate the sum of digits of a given number
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# In[ ]:




