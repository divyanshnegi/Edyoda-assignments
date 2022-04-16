#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Write a Python program to get the Fibonacci series between 0 to 50.
f=0
s=1
sum=0
for i in range(0,50):#for loop
    if s<=50:
       print(s,end=" ")
       sum=f+s
       f=s
       s=sum
       
    else:
       exit(0)

