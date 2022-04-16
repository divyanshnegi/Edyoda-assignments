#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.
n=[1,2,3,4,5,6,7,8,9]#list
c=0
d=0
for i in n:#for loop
  if i%2==0:
    c+=1
  else:
    d+=1
#print function
print("Number of even numbers",c)  
print("Number of odd numbers",d) 


# In[ ]:




