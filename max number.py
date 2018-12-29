#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a program to accept 'n' numbers from user,store these  numbers into an array.
#find out maximum and minimum number from an array
num=[]
n=int(input("how many numbers you want to enter"))
for i in range(1,n+1,1):
    x=int(input("enter a number"))
    num.append(x)
print("the numbers in the array are",num)
print("max number in the array is",max(num))
print("min number in the array is",min(num))


# In[ ]:




