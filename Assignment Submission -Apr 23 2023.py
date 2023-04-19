#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Read the dataset to python environment

# In[6]:


dataframe=pd.read_excel(r"C:\Users\anjup\Downloads\iris (1).xls")


# In[7]:


dataframe


# # Display the columns in the dataset.

# USING LOC

# In[11]:


dataframe.loc[:,'SL']


# In[12]:


dataframe.loc[:,'SW']


# In[14]:


dataframe.loc[:,'PL']


# In[15]:


dataframe.loc[:,"PW"]


# In[16]:


dataframe.loc[:,'Classification']


# In[20]:


dataframe.loc[:,["SL","SW","PL","PW","Classification"]]


# USING ILOC

# In[21]:


dataframe.iloc[:,0]


# In[22]:


dataframe.iloc[:,1]


# In[23]:


dataframe.iloc[:,2]


# In[24]:


dataframe.iloc[:,3]


# In[25]:


dataframe.iloc[:,4]


# In[33]:


dataframe.iloc[:,[0,1,2,3,4]]


# # Calculate the mean of each column of the dataset

# In[35]:


dataframe.mean()


# # Check for the null values present in the dataset.

# In[38]:


dataframe.isnull()


# In[39]:


dataframe.isnull().sum()


# # Perform meaningful visualizations using the dataset.Bring at least 3 visualizations.

# In[83]:


plt.figure(figsize=(6,6))
sns.boxplot(x=dataframe['Classification'],y=dataframe["SL"])
plt.title("Visualization of Sepal Length and Classification using box plot")
plt.show()


# In[82]:


sns.countplot(x=dataframe['Classification'])
plt.title("Visualization of Count on Classification using count plot")
plt.show()


# In[81]:


plt.figure(figsize=(7,7))
plt.scatter(dataframe["PL"],dataframe["PW"])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title('Visualization of petal length and petal width using scatter plot')
plt.show()


# In[80]:


plt.bar(dataframe['Classification'],dataframe['PL'])
plt.xlabel('Classification')
plt.ylabel('Petal Length')
plt.title("Visualization of Classification and Petal Length using Bar chart")
plt.show()


# In[ ]:




