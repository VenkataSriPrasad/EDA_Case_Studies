#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[147]:


df = pd.read_csv(r"C:\Users\Venkat Sri Prasad\Downloads\Car details v3.csv")
df


# In[148]:


del df['torque']
#Removing Torque because the data is so inconsistent


# In[150]:


#Removing Special Characters in Columns
a = df.columns[df.isnull().any()]
print(a)
for i in a:
    df[i] = df[i].replace(r'[^\d.]+', '')
df


# In[151]:


#Converting String DataTypes into Float dataTypes
for i in a:
    df[i] = df[i].fillna(0)
    df[i] = df[i].replace("",'0')
    
b = df.select_dtypes(include=['int64', 'float64']).columns
df[a] = df[a].astype(float)
print(df.dtypes)


# In[152]:


df.info()


# In[153]:


df.describe()


# In[154]:


#Replacing the Null Values with Median Values

b = df.select_dtypes(include=['int64', 'float64']).columns
c=[]
for i in b:
    df[i]=df[i].replace(0,df[i].median())
df


# In[155]:


df.isnull().sum()
#NO NULL Values


# In[107]:


nulls_percentages = df.isnull().sum() /len(df)*100
columns_with_high_nulls = nulls_percentages > 25

columns_with_high_nulls_list = nulls_percentages[columns_with_high_nulls].index.tolist()
columns_with_high_nulls_list


# In[156]:


import seaborn as sns


# In[157]:


sns.distplot(df["seats"])


# In[216]:


import matplotlib as plt
import numpy as np
df = pd.DataFrame(data = np.random.random(size=(4,7)), columns = b)
df.boxplot()


# In[217]:


sns.boxplot(y='km_driven',data=df)


# In[218]:


df1= df[df['max_power']<0.8]
df1_median=df1.median()
df.loc[df['max_power'] >0.8 , 'max_power' ]= df1_median
df2= df[df['km_driven']<0.8]
df2_median=df2.median()
df.loc[df['km_driven'] >0.8 , 'km_driven' ]= df2_median


# In[219]:


sns.boxplot(y='km_driven',data=df)


# In[221]:


import matplotlib as plt
import numpy as np
df = pd.DataFrame(data = np.random.random(size=(4,7)), columns = b)
df.boxplot()


# In[ ]:




