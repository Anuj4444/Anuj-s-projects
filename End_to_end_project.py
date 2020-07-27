#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[10]:


norm_data = pd.DataFrame(np.random.normal(size=100000))
skewed_data = pd.DataFrame(np.random.exponential(size=100000))
print(norm_data)
print(skewed_data)


# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
norm_data.plot(kind="density",figsize=(10,10),xlim=(-1,5))
plt.vlines(norm_data.mean(), ymin=0, ymax=0.8, linewidth=5.0)
plt.vlines(norm_data.median(),ymin=0,ymax=0.8,linewidth=2.0,color="red")


# In[16]:


skewed_data.plot(kind="density",figsize=(10,10),xlim=(-1,5))
plt.vlines(skewed_data.mean(), ymin=0, ymax=0.8, linewidth=5.0)
plt.vlines(skewed_data.median(),ymin=0,ymax=0.8,linewidth=2.0,color="red")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




