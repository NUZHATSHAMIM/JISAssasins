#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 16
##Write a Program to Accept character and display its
# Ascii value and its Next and Previous Character.
#chr() for ascii to char
x= input("Enter the input :")
n= ord(x)
prev= n - 1
next= n + 1
a=chr(prev)
b=chr(next)
print(" ASCII value is : ",n)
print("The previous value is : ",a)
print("The next value is : ",b)


# In[ ]:




