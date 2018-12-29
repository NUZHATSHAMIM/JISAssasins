#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a program to calculate the sum of first digit and the last digit of a given number
n = int(input("Enter a Number :"))

p = 0
f = 0
s = 0

l = n % 10

while n > 0:
    r = n % 10

    p= p * 10 + r

    n = int(n / 10)
    
f = p % 10

s = f + l

print("Sum of first and last digit is :", s)


# In[ ]:




