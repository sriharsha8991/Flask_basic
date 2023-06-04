#!/usr/bin/env python
# coding: utf-8

# ## EDA on ZOMATO Data set

# In[2]:


#importing Required Libraries For our Exploratory Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# #### Before diving into the actual coding part check out the CSV and Excel Files we have inorder to get the better Understanding

# In[3]:


df1 = pd.read_csv('zomato.csv')
df2 = pd.read_excel('Country-Code.xlsx')

df1.head(5)


# In[4]:


#we have 2 data files here one is our zomato data set and the other its respective Country codes
#in the coming codes we are going to "merge" them
zdf = pd.merge(df1,df2, on = 'Country Code')
zdf.head()
# Now we have both country code country are on same datasets


# In[5]:


zdf.info()
#it gives an overview of our dataset


# #from the above "info" we can find out there are few null values in Cuisines column,  
# but the number of null values are negligible when compared with 9000 rows

# In[6]:


zdf.dropna(inplace = True)
zdf.info()


# In[7]:


##Now lets see how many countries are represented in the data set and
##how many restaurants each country has in the data.
zdf.Country.value_counts()


# ### observations

# 1.we can see 15 countries listed inour dataset and no. of restaurents in each country
# 2.we can also see that the maximum no. of listings are from INDIA.
# 3.we can make sure from the above data that it is a INDIAN Ccompany.

# So it makes sense to have some analysis for the data of Indian restaurants.
# #### Lets see top 10 cities in India represented in the data set.

# In[18]:


zdf.loc[zdf['Country'] == 'India'].City.value_counts().head(10)
#.reset_index()
#.rename(columns = {'index':'City','City':'count'})


# In[16]:


zdf.loc[zdf['Country'] == 'India'].City.value_counts().head(10).reset_index()


# In[17]:


zdf.loc[zdf['Country'] == 'India'].City.value_counts().head(10).reset_index().rename(columns = {'index':'City','City':'Count'})


# ### observations

# 1.the maximum no. of restuarents are From New Delhi
# 

# ### lets consider some Indian Resturents
# 

# In[19]:


# we are making a data frame that only consists of Indain Restos...
z_ind = zdf.loc[zdf['Country'] == 'India']
z_ind.head(3)


# In[ ]:





# In[20]:


# Now we will go back to our columns once again in indian data set of zomato
z_ind.info()


# In[24]:


# we will find out If there is any relation between "average cost for two "and "aggregate rating of restaurants".

z_ind.plot.scatter(x='Average Cost for two',y='Aggregate rating',figsize=(10,6), color='blue', title="Cost vs Agg Rating")


# #### Observations
#  From the above graph, we can see that most of the data is clustered around cost upto 2000 and rating values from 2 to 4.5 approximately. There are few restaurants with cost range between 2500 to 6000.

# In[25]:


#Better view of relation between average cost for two and aggregate rating of restaurants
sns.jointplot(x='Average Cost for two',y='Aggregate rating',kind ='hex',gridsize=18,data =z_ind,color='red')


# ###### In above graph, we can see more clearly that the maximum number of rating values are around 3 to 3.5 and the 'Avg cost for two, for maximum data is also up to 1000.

# In[37]:


#Top 10 Cuisines served by restaurants
z_cuis = z_ind['Cuisines'].value_counts().sort_values(ascending=False).head(10)
z_cuis.plot(kind = 'pie',figsize=(14,8), 
title="Most Popular Cuisines", autopct='%.2f%%')
plt.axis('equal')


# ### Observations
# From the above graph, we can clearly see that 'North Indian' cuisine is the most popular cuisine

# ## Now lets do something with our ratings in the data set

# In[45]:


ratings=zdf.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index()


# In[46]:


ratings


# In[43]:


ratings=zdf.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[42]:


ratings


# In[40]:


zdf.groupby(['Aggregate rating','Country']).size().reset_index().head().rename(columns = {0:'total'})


# ### observation
# Maximum number of zero ratings are from india
# we can have 2 conclusions here
# 
# 1.Since data is mostly inclined towards indians there is a chance of high 0 ratings from india
# 
# 2.the chance of no rating is can also be considered as zero

# In[48]:


# which Countries Do have online deliveries

#zdf[zdf['Has Online delivery'] =="Yes"].Country.value_counts()

# we can also see entire data using group by method
zdf[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# ### observation
# Online deliveries of Zomato are availabale in India and Uae only
# 

# In[51]:


z_corr = zdf[['Average Cost for two', 'Price range', 'Aggregate rating']]
sns.heatmap(z_corr.corr(),linewidth=1.0,annot = True)


# #### We can see 'price range'-'agg rating' appear to be correlated upto an extent 

# In[ ]:


#you can also explore various other questions which are as follows


# ### try it out Questions
# 1.correlations between top 5 cities and prices
# 
# 2.what are the kind of currencies used in different countries and its effects
# 
# 3.how city and table bookings are effected between each other and many more
# 
