#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt


# In[91]:


df = pd.read_csv('Breast_cancer_data.csv') 
df.head()


# In[92]:


#plt.scatter(df.Age,df.Outcome,marker='+',color='red')


# In[93]:


df.shape


# In[94]:


from sklearn.model_selection import train_test_split


# In[150]:


X_train, X_test, y_train, y_test = train_test_split(df[['mean_radius','mean_texture','mean_perimeter','mean_area','mean_smoothness']],df.diagnosis,train_size=0.75)


# In[151]:


X_test


# In[152]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


# In[153]:


model.fit(X_train, y_train)


# In[154]:


y_predicted = model.predict(X_test)


# In[155]:


model.predict_proba(X_test)


# In[156]:


model.score(X_test,y_test)


# In[123]:


y_test


# In[124]:


X_test


# In[125]:


#data = [[4,91,70,32,88,33.1,0.446,22]]
#from sklearn.svm import LinearSVC


# In[161]:


import pickle


# In[162]:


pickle.dump(model, open('prediction.pickle', 'wb'))


# In[ ]:




