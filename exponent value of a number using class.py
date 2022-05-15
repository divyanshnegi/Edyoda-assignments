#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Power:#class
    def __init__(self,num,times):#init method
        self.num=num
        self.times=times
    def result(self):#class for result display
        print(pow(self.num,self.times))
            
x=int(input())
n=int(input())            
obj=Power(x,n)#object
obj.result()


# In[ ]:




