#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Sort_it(x):  
        
    n= len(x)  
    for i in range(0,n):  
            
        for j in range(0,n-i-1):  
            if (x[j][-1]>x[j+1][-1]):  
                z=x[j]  
                x[j]=x[j+1]  
                x[j+1]=z
    return x  
    

list_tuple=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
          
print(Sort_it(list_tuple))

