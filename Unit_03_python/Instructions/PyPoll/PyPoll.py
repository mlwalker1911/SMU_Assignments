#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


file = "Resources/election_data.csv"
Election_df = pd.read_csv(file)
Election_df


# In[14]:


Total_Votes_df =Election_df["Voter ID"].count()
Total_Votes_df


# In[5]:


Election_df["Candidate"].unique()


# In[9]:


Election_df["Candidate"].value_counts()


# In[15]:


Election_df["Candidate"].value_counts() / Total_Votes_df


# In[17]:


Election_df["Candidate"].value_counts().idxmax()


# In[ ]:




