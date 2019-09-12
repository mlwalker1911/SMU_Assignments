#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


file = "Resources/budget_data.csv"
Budget_df = pd.read_csv(file)
Budget_df


# In[10]:


Budget_df["Date"].count()


# In[11]:


Budget_df["Profit/Losses"].sum()


# In[22]:


Budget_df["Changes"] = Budget_df["Profit/Losses"].diff()


# In[23]:


Budget_df.head()


# In[24]:


Budget_df["Changes"].mean()


# In[25]:


Budget_df["Changes"].min()


# In[26]:


Budget_df["Changes"].max()


# In[34]:


minrow = Budget_df["Changes"].idxmin()
Budget_df.iloc[minrow,].Date


# In[35]:


maxrow = Budget_df["Changes"].idxmax()
Budget_df.iloc[maxrow,].Date


# In[ ]:




