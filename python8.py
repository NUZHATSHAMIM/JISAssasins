#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a program to swap the values of two variables using call by reference:by nuzhat shamim
x = 5
y = 10

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y)

