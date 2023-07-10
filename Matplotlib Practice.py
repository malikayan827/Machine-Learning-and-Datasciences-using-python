#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

plt.style.use('classic')
x=np.linspace(0,100,1000)
y=np.cumsum(np.random.randn(1000,5),0)
plt.plot(x,y)
plt.legend('ABCDE',ncol=2,loc='upper left')


# In[4]:


sns.set()
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2,loc='upper left')


# In[6]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

plt.hist(X)


# In[9]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

plt.hist(X,alpha=0.5,density=True)


plt.hist(Y,alpha=0.5,density=True)


# In[10]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

plt.hist(X,alpha=0.5,density=True)
plt.hist(Z,alpha=0.5,density=True)
plt.hist(Y,alpha=0.5,density=True)


# In[11]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

data.head()


# In[12]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

for col in data.columns:
    plt.hist(data[col], density=True , alpha=0.5)


# In[14]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

for col in data.columns:
    plt.hist(data[col], density=True , alpha=0.5)
    sns.kdeplot(data[col], fill=True)


# In[20]:


sns.set()
X=pd.Series(50*np.random.randn(5000))
Y=pd.Series(200*np.random.randn(5000))
Z=pd.Series(100*np.random.randn(5000)+500)
data=pd.DataFrame({'X':X,'Y':Y,'Z':Z})

for col in data.columns:
    sns.distplot(data[col])


# In[26]:


import seaborn as sns

with sns.axes_style('white'):
    sns.jointplot(x="X", y="Y", data=data, kind='kde')


# In[27]:


sns.pairplot(data)


# In[ ]:




