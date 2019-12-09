#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
from datetime import datetime


# In[122]:


data = pd.read_excel(open('test.xlsx', 'rb'),sheet_name='Sheet1')


# In[124]:


newArray = []


# In[131]:


def manageRow(th1, mi, idx):
    while(mi / 60 >= 1):
        newArray.append({'time': data.iloc[idx,0], 'duration1': data.iloc[idx,1], 'duration2': data.iloc[idx,2], 'periodOfDay': th1, 'touchMins': 60})
        mi -= 60
        th1 += 1
    if(th1 >= 25):
        th1 = 0
    if(mi < 60):
        newArray.append({'time': data.iloc[idx,0], 'duration1': data.iloc[idx,1], 'duration2': data.iloc[idx,2], 'periodOfDay': th1, 'touchMins': mi})


# In[128]:


for idx, i in enumerate(data.iterrows()):
    th1 = data.iloc[idx,0].hour 
    tm1 = data.iloc[idx,0].minute 
    
    dh1 = data.iloc[idx,1].hour 
    dm1 = data.iloc[idx,1].minute
    dh2 = data.iloc[idx,2].hour 
    dm2 = data.iloc[idx,2].minute
    
    mi = tm1 + dm1 + dm2
    hr = (dh1 + dh2) * 60

    mi += hr
    manageRow(th1, mi, idx)


# In[132]:


df = pd.DataFrame(newArray)
df

