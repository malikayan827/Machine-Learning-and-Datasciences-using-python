#!/usr/bin/env python
# coding: utf-8

# In[7]:


#making an array of all zeroes
import numpy as np
print(np.zeros(10));


# In[8]:


#making an array of all ones
import numpy as np
print(np.ones(10));


# In[18]:


#making an array of all fives
import numpy as np
print(np.full(10,5));


# In[21]:


#making an array of all 10 to 50
import numpy as np
print(np.arange(10,51,1));


# In[22]:


#making an array of all 10 to 50 all even
import numpy as np
print(np.arange(10,51,2));


# In[26]:


#making an 3*3 identity matrix
import numpy as np
matrix1 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matrix1)


# In[27]:


#generating random number b/w 0 and 1
import numpy as np
print(np.random.rand(1,1))


# In[29]:


#matrix 3*3 with values b/w 0 to 8
matrix = np.random.randint(0, 9, size=(3, 3))
print(matrix)


# In[30]:


#generating random number 25 random numbers from a 
#from a standard normal distribution
random_numbers = np.random.randn(25)
print(random_numbers)


# In[34]:


#making an array of all 0 to 1 with step of 0.01
import numpy as np
print(np.arange(0,1.01,0.01));


# In[36]:


#create an array of 20 linearly spaced points b/w 0 ad 1
import numpy as np
print(np.linspace(0,1,20));


# In[49]:


#indexing and slicing
mat=np.arange(1,26).reshape(5,5)
print(mat);


# In[50]:


mat=mat[2:]


# In[51]:


mat


# In[52]:


mat=mat[:,1:]


# In[53]:


mat


# In[60]:


mat=np.arange(1,26).reshape(5,5)
print(mat);


# In[66]:


array=mat[:,1:-3]
array=array[:-2,:]
array


# In[70]:


mat=np.arange(1,26).reshape(5,5)
print(mat);


# In[71]:


array=mat[3:,:]


# In[72]:


array


# In[73]:


#some  operations on mat
#sum
mat=np.arange(1,26).reshape(5,5)
print(mat);


# In[77]:


sum=0
for element in np.nditer(mat):
  
   sum=element+sum
sum    


# In[78]:


mat=np.arange(1,26).reshape(5,5)
print(mat);


# In[79]:


#standard deviation
std_dev = np.std(mat)

print("Standard Deviation:", std_dev)


# In[81]:


#sum of columns
mat=np.arange(1,26).reshape(5,5)
column_sums = np.sum(mat, axis=0)

print("Column Sums:", column_sums)



# In[ ]:




