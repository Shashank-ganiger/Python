#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Python Program to Solve Quadratic Equation
#Solve the quadratic equation ax**2 + bx + c = 0

#import complex math module
import cmath

a = 1
b = 5
c = 6

#calculate the discriminant
d = (b**2) - (4*a*c)

#find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('the solutions are {0} and {1}'.format(sol1,sol2))


# In[7]:


#Python Program to Swap Two Variables

x = 5
y = 10

#to take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping : {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[8]:


#Python Program to Swap Two Variables

x = 5
y = 10o
z = 6

#to take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')
#z = input('Enter value of z: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp
y = z
z = temp


print('The value of x after swapping : {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('The value of z after swapping: {}'.format(z))


# In[9]:


#program to generate a random number between 0 and 9

#importing the random module
import random

print(random.randint(0,9))


# In[10]:


#program to generate a random number between 0 and 9

#importing the random module
import random

print(random.randint(0,9))


# In[11]:


#program to generate a random number between 15 and 20

#importing the random module
import random

print(random.randint(15,20))


# In[12]:


#program to generate a random number between 15 and 20

#importing the random module
import random

print(random.randint(15,20))


# In[13]:


#taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles 
miles = kilometers * conv_fac
print ('%0.2f kilometer is equal to %0.2f miles'%(kilometers, miles))


# In[14]:


#taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles 
miles = kilometers * conv_fac
print ('%0.2f kilometer is equal to %0.2f miles'%(kilometers, miles))


# In[15]:


#taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#conversion factor
conv_fac = 0.621371

#calculate miles 
miles = kilometers * conv_fac
print ('%0.2f kilometer is equal to %0.2f miles'%(kilometers, miles))


# In[16]:


#taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

#conversion factor
conv_fac = 0.621371

#Enter a value of kilometers
a = 1

#calculate miles 
miles = kilometers * conv_fac
print ('%0.2f kilometer is equal to %0.2f miles'%(kilometers, miles))


# In[ ]:




