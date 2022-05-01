#!/usr/bin/env python
# coding: utf-8

# In[19]:


string="The quick Brow Fox"

def upper(s1):
    count_U=0
    for i in s1:
        if (i.isupper())==True:
            count_U+=1
    print("No. of Upper case characters:",count_U) 
    
def lower(s2):
    count_L=0
    for j in s2:
        if (j.islower())==True:
            count_L+=1
    print("No. of Lower case Characters:",count_L) 
            
upper(string)       
lower(string)


# In[ ]:




