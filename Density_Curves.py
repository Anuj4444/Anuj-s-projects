#!/usr/bin/env python
# coding: utf-8

# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[24]:


from ggplot import mtcars
header_data = mtcars.head()
print(header_data)


# In[25]:


header_data.describe()


# In[26]:


mtcarsMeanCarWise = mtcars.mean(axis=0)
print(mtcarsMeanCarWise)


# In[27]:


medianCarsFeatures = mtcars.median(axis=1)
print(medianCarsFeatures)


# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
mtcars.hist(bins=10, figsize=(20,15))
plt.show


# In[29]:


for cols in mtcars.columns:
    if (cols != "name"):
        mtcars[cols].plot(kind="density", figsize=(2,2))
        plt.title(cols)
plt.show()


# In[30]:


from pandas.plotting import scatter_matrix
attributes = ["mpg", "disp", "hp", "wt", "qsec"]
scatter_matrix(mtcars[attributes], figsize=(12,8))
plt.show


# In[31]:


mtcars.skew()


# In[39]:


for cols in mtcars.columns: 
    if (cols != "name"): 
        print(mtcars[cols].describe()) 
print(cols + ": " + str(mtcars[cols].quantile(0.75) - mtcars[cols].quantile(0.25)))


# In[43]:


mtcars["mpg"].plot.box() 
pd.DataFrame(mtcars["mpg"]).boxplot()


# In[47]:


mtcars["mpg"].describe()


# In[48]:


mtcars["mpg"].var()


# In[49]:


mtCarsAutomatic = mtcars[mtcars["am"]==0]
mtCarsManual = mtcars[mtcars["am"]==1]
print(mtCarsAutomatic)
print(mtCarsManual)


# In[50]:


pd.DataFrame(mtcars[["mpg","am"]]).boxplot(by="am")


# In[58]:


mtcars["mpg"].mean()


# In[59]:


mtcars["mpg"].var()


# In[ ]:





# In[ ]:




