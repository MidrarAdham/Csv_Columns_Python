#!/usr/bin/env python
# coding: utf-8

# In[86]:


import pandas as pd
import numpy as np
#df = pd.read_csv("test.csv", index_col = 0)
household = pd.read_csv(r'/Users/midrar/Desktop/PSU/EXCEL_TO_CSV/test2.csv', index_col = 0)
household


# In[128]:


i = 1
k = 0
j = 0
for row in household:
    d = household.iloc[:, k:i]
    print (d)
    i = i + 1
    k = k + 1
    Path = '/Users/midrar/Desktop/PSU/EXCEL_TO_CSV/converted/'+str(j)+'.csv'
    d.to_csv(Path)
    j = j + 1
    if i == 6:# and k == 1:
        break


# In[101]:





# In[ ]:





# In[ ]:




