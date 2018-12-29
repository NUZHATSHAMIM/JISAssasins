#!/usr/bin/env python
# coding: utf-8

# In[2]:


#write a menu driven program to perform the following operations on string using standard library functions:by nuzhat shamim
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = "Nuzhat"
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")



# In[ ]:




