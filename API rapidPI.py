#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {"ingr":"champagne"}

headers = {
    "X-RapidAPI-Key": "2eea4dfd68msh73ab0be3bab537ep1fd69ejsne1b0d3a94597",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# Extraction des 10 premiers produits et créat
productsall = response.json()

data = []
for product in productsall['hints'][:10]:
    food = product['food']
    data.append({
        'foodId': food['foodId'],
        'label': food['label'],
        'category': food['category'],
        'foodContentsLabel': food.get('foodContentsLabel', ''),
        'image': food.get('image', '')
    })
    
# Create a pandas dataframe from the extracted data
df = pd.DataFrame(data, columns=['foodId', 'label', 'category', 'foodContentsLabel', 'image'])


# Save the dataframe to a CSV file
df.to_csv('API Edamam Food and Grocery Database.csv', index=False)

df


# In[2]:


df.image[0]


# In[3]:


productsall.keys()


# In[4]:


productsall


# In[5]:


productsall['text']


# In[6]:


productsall['parsed']


# In[7]:


productsall['hints']


# In[8]:


productsall['_links']


# In[9]:


len(productsall['hints'])


# In[10]:


productsall['hints'][0]


# In[11]:


from PIL import Image
import matplotlib.pyplot as plt
list_url = [url for url in df.image.unique() if url !='']
for i in range(len(list_url)):
    plt.subplot(130  + i +1)
    im = Image.open(requests.get(list_url[i], stream=True).raw)
    plt.imshow(im)

