#!/usr/bin/env python
# coding: utf-8

# # Data Loading, Pre-Processing and Cleaning

# In[56]:


# importing helpful files
import numpy as np
import pandas as pd


# In[277]:


csv_data = pd.read_csv("csv_file/covid-trade-2020.csv")


# In[278]:


csv_data.head(10)


# In[58]:


csv_data.shape


# # Summary statistics
# csv_data.describe()

# In[60]:


# Viewing the columns in the dataset
csv_data.columns


# In[61]:


# Viewing the dataset of each column
csv_data.dtypes


# In[64]:


csv_data.isnull().sum(axis = 0)


# In[70]:


# Plotting the boxplot to view the exceptionally out of boundaries values

import matplotlib.pyplot as plt 
plt.boxplot(csv_data['Cumulative'])


# In[69]:


plt.boxplot(csv_data['Value'])


# ### As most of the values forming clusters thats why they are not forming any outliers values

# # Data Analysis And Visualization

# In[279]:


# Grouping by 'Year','Country', 'Direction', 'Transport_Mode' to filter out lot of rows and see the trade trends

updated_csv = csv_data.groupby(['Year','Country', 'Direction', 'Transport_Mode'], as_index=False)['Value', 'Cumulative'].sum()


# In[187]:


updated_csv.head(10)


# In[262]:


# Lets check the again shape. Now it should have reduced

updated_csv.shape


# In[263]:


# Seeing for which counteries Export and Imports are mostly done

plt.rcParams["figure.figsize"] = (8,5)
updated_csv.plot.scatter(x = 'Direction', y = 'Country', c = 'blue')


# In[264]:


# Plotting the year vs Value to look for the trend in each year

pltdata:image/png;base64,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.rcParams["figure.figsize"] = (8,5)
updated_csv.plot.scatter(x = 'Year', y = 'Value', c = 'blue')


# In[265]:


plt.rcParams["figure.figsize"] = (10,5)
plt.plot(updated_csv['Year'], updated_csv['Value'])


# ### Here in above graph you can see, just when the trade values are going upward from 2016-2019; 2020 is showing relatively downward trend of trade.

# # Analysis of how much imports and exports effected in covid-19

# In[266]:


# Analysis of data and view the Exports and Imports seperately

new_data = updated_csv.groupby(['Direction', 'Year']).sum()
new_data.shape


# In[267]:


new_data.head(18)


# In[268]:


new_data.loc['Imports'].diff().plot()
plt.legend()


# In[269]:


new_data.loc['Exports'].diff().plot()
plt.legend()


# In[270]:


new_data.loc['Reimports'].diff().plot()
plt.legend()


# # Analysis on the basis of transport mode how transport effects the trade in Covid-19

# In[271]:


# Analysis of data how transport_mode effected the trade

transport_data = updated_csv.groupby(['Transport_Mode', 'Year']).sum()
transport_data.shape


# In[272]:


transport_data.head(18)


# In[276]:


# Looking how much trade effected by air transport

transport_data.loc['Air'].diff().plot()
plt.legend()


# In[274]:


transport_data.loc['Sea'].diff().plot()
plt.legend()


# In[275]:


transport_data.loc['All'].diff().plot()


# In[ ]:





# In[ ]:




