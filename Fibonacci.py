#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

    


# In[2]:


#Write a Python program that accepts a word from the user and reverse it.
def revst(a):#function defined
    a=a[::-1]
    return a

x=revst(input("enter a word"))#main function
print(x)


# In[1]:


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




