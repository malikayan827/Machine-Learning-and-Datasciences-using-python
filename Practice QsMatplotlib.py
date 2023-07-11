#!/usr/bin/env python
# coding: utf-8

# In[5]:


#making an html file using bokeh plot
from bokeh.plotting import figure, output_file, show
output_file("demo.html")
p=figure(width=400,height=400,title="line")
p.line([1,2,3,4,5],[6,7,8,9,10],line_width=2)
show(p)


# In[12]:


import numpy as np
from bokeh.plotting import figure, show

p = figure(width=800, height=800, title="bokeh Example", x_axis_label='X', y_axis_label='Y')
x = np.linspace(0, 10, 30)
y1 = np.sin(x)
y2 = np.cos(x)

p.line(x, y1, legend_label="y=sin(x)")
p.circle(x, x, legend_label="y=x", fill_color="green", size=5)
p.line(x, y2, legend_label="y=cos", line_width=3, line_color="red")
p.triangle(x,x**2,color='black')
show(p)


# In[17]:


from bokeh.layouts import gridplot
x=np.linspace(0,6*np.pi,100)
y0=np.sin(x)
y1=np.cos(x)
y2=np.sin(x) + np.cos(x)-1
s1=figure(width=400)
s1.circle(x,y0,size=10,color="navy",alpha=0.5)
s2=figure(width=400)
s2.triangle(x,y0,size=10,color="navy",alpha=0.5)
s3=figure(width=400)
s3.triangle(x,y0,size=10,color="navy",alpha=0.5)
p=gridplot([[s1,s2,s3]])

show(p)


# In[20]:


import numpy as np
x=np.arange(0,100)
y=x*2
z=x**2


# In[23]:


#excercise 1
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('graph')


# In[24]:


#excercise 2

fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y)
ax2.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('graph')



# In[28]:


#excercise 3

fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,z)
ax2.plot(x,y)

ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax2.set_xlim([20,22])
ax2.set_xlim([30,50])

ax2.set_title('zoom')



# In[30]:


#excercise 4
fig,axes=plt.subplots(1,2,figsize=(12,2))
axes[0].plot(x,y,color='blue',lw=3,ls='--')
axes[1].plot(x,z,color='red',lw=3)


# In[ ]:




