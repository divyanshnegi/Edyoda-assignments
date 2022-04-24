#!/usr/bin/env python
# coding: utf-8

# In[16]:


def incordersort(x):
    return sorted(x, key=last_element)

def last_element(y):
    return y[-1]

l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(incordersort(l1))

