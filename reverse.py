#!/usr/bin/env python
# coding: utf-8

# In[1]:


#write a program to accept a sentence from the user and reverse its each word
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")
print("\n")


# In[ ]:




