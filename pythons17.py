#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q17. Write a program to accept n numbers and store all the prime nos in an array and display the array.:by nuzhat shamim
x= input('enter the set of numbers :(enter space seperatedvalue):')
list1= x.split(" ")
res=[]
for i in list1:
    n = int(i)
    for j in range(2,int(n/2)):
        if(n%j == 0):
            break
    else:
        res.append(n)
print(res)


# In[ ]:




