#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#write a program to accept four digits number from user and count zero,odd and even digits from the entered number.
class Count:
    def counting(self,num):
        i=0
        e=0
        o=0
        z=1
        count=4
        while(count>0):
            z=x%10
            if z == 0:
                i+=1
                elif z%2 !=0:
                    e+=1
                    elif z%2 !=0:
                        o+=1
                        x=x//10
                        count-=1
                        print("Zeroes={},Even={},odd={}".format(i,e,o))
c=Count()
num=int(input("Enter a four digit number:"))
c.counting(num)

