#!/usr/bin/env python
# coding: utf-8

# In[22]:


from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


a=np.array([1,2,3])
b=np.array([6,7,8,9])


# In[6]:


a,b=np.meshgrid(a,b)


# In[8]:


print(a)
print(b)


# In[13]:


plt.style.use("seaborn")


# In[16]:


fig=plt.figure()
axes=fig.gca(projection='3d')
axes.plot_surface(a,b,a+b,cmap="coolwarm")
plt.show()


# In[18]:


# parabola Shaped Surface Plots
a=np.arange(-1,1,0.01)
b=a
a,b=np.meshgrid(a,b)


# In[20]:


fig=plt.figure()
axes=fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap="rainbow")
plt.title("Surface Plots")
plt.show()


# In[23]:


# Contour Plots

fig=plt.figure()
axes=fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap="rainbow")
plt.title("Contour Plots")
plt.show()


# In[ ]:




