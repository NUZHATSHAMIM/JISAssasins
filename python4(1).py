#!/usr/bin/env python
# coding: utf-8

# In[2]:


#program to accept 'n' numbers from user store these numbers into an array and sort 
num = int(input("How many figures:"))
storage = []
result = []
for i in range (1,num+1):
    a = int(input("Enter value" + str(i) + " : "))
    storage.append(a)
for m in range(len(storage)):
    b = min(storage)
    storage.remove(b)
    result.append(b)
j = ' '.join(str(i) for i in result)
print(j)


# In[ ]:




