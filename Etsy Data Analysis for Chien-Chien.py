#!/usr/bin/env python
# coding: utf-8

# # Etsy Data Analysis for Chien-Chien

# Data Analysis compiled and executed by **Max Chen**
# 
# Last updated on: **March 30th 2025**

# ## Introduction

# The following analysis contains the "Etsy Retail Products" data set from 2021, and focuses on examining the product catelogues within the Etsy e-commerce platform for Chien-Chien. Given the direction of the client's e-commerce brand, Chien-Chien, the following **Areas of Interest** were devised and designed to find similar sellers/brands on Etsy; certain questions include sub-categories of **Painting** and **Paper** as they require further filtering. 
# 
# After data wrangling is completed, the analysis will begin as each area of interest will be tackled individually with appropriate visualizations and dataframe results. Each category (and their sub-categories) will include the answers to the following questions:
# 
# 1. Are there any null values?
# 2. What is the mean, standard deviation and count of each quantitative columns?
# 3. A graphical visualization of the filtered dataframe.
# 4. What are the categories associated with each product in the filtered dataframe?
# 5. How does the filtered dataframe look when sorted by the highest to lowest for "Average Rating"?
# 6. Who are the sellers/brands (including the Etsy link)? 
# 
# As each area of discussion wraps up, a brief conclusion statement will be included. 
# 
# At the end of the analysis, an overall conclusion will be provided, as well as a SWOT analysis. 

# ## Areas of Interest

# Areas to focus on:
# 1. Gift
#     (1) Painting
#     (2) Paper
# 2. Decor
#     (1) Painting
#     (2) Paper
# 3. Chinese
# 4. Japanese
# 5. Custom
#     (1) Painting
#     (2) Paper
# 6. Color Print
# 7. Handmade Paper

# ## Data Wrangling

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install altair vega_datasets')


# In[1]:


# import necessary libraries
import pandas as pd
import altair as alt
import json as json
import numpy as np


# In[2]:


# read in the data set
etsy = pd.read_json('etsy.json')
etsy


# In[3]:


etsy.info()


# In[4]:


etsy.describe()


# Given the analysis does not require all of the columns, three will be removed, which are "availability", "images", and "scraped_at".

# In[5]:


etsy = etsy.drop(columns=['availability', 'images', 'scraped_at'])
etsy


# With the original data set being a "json" file, there's some odd text in the "product_details"; these weird "\n\n\n\n\n\n" will be replaced by a simple ", ".

# In[6]:


# replace the '\n\n\n\n\n\n' with ', '
etsy['product_details'] = etsy['product_details'].str.replace('\n\n\n\n\n\n', ', ')
etsy


# ## Exploratory Data Analysis

# ### "Gift" Main Category

# In[7]:


# Find the rows with the word 'Gift' in the "description" column
etsy_gift = etsy[etsy['description'].str.contains('Gift')]
etsy_gift


# In[8]:


etsy_gift.info()


# In[9]:


etsy_gift.describe()


# As shown in the results above, the "Gift" dataframe includes 421 non-null rows with a **mean of 43.89** and a **standard deviation of 60.28**. However, this category is simply too all-encompassing, so it will be further divided into more appropriate subcategories of **Painting** and **Paper** instead.

# ### Creating the dataframe for the subcategory of 'Painting' in the main category, "Gift". ###

# In[11]:


etsy_gift_painting = etsy_gift[etsy_gift['description'].str.contains('Painting')]
etsy_gift_painting


# In[14]:


etsy_gift_painting.info()


# In[15]:


etsy_gift_painting.describe()


# In[16]:


etsy_gift_painting_pricemean = 95.87
etsy_gift_painting_pricemean


# The "etsy_gift_painting" dataframe includes 10 rows with a **mean of 95.87** and a **standard devaition of 66.56** for "price". There is a signifcant deifference between the most and least expensive products, which equates to **185.40**; such a drastic contrast showcases how differently each seller/brand/artist prices their own work/product. 
# 
# Below is a Bar Chart to visually illustrate the difference of prices within this dataframe.

# In[17]:


# create a Bar Chart with each brand as X and price as Y
etsy_gift_painting_bar = alt.Chart(etsy_gift_painting).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    opacity=0.8,
    color='purple')

etsy_gift_painting_bar


# In[18]:


# Unique cateory in etsy_gift_painting
etsy_gift_painting_category = etsy_gift_painting['category'].unique().tolist()
etsy_gift_painting_category


# Most products seem to be included within the "Pet Supplies" category, with a few branching out to "Art & Colectibles". 

# In[19]:


# sort value by average_rating
etsy_gift_painting_sort = etsy_gift_painting.sort_values(by=['average_rating'], ascending=False)
etsy_gift_painting_sort


# Despite the lesser review counts, **LetitiasArt is the highest reviewed seller on average** in etsy_gift_painting. Let's take a look at all the seller and assess which one may be better aspirations for Chien-Chien.

# In[20]:


# Unique brand in etsy_gift_painting
etsy_gift_painting_brand = etsy_gift_painting['brand'].unique().tolist()
etsy_gift_painting_brand


# Link to **NadineSophieArt** on Etsy (deactivivated): n/a

# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# Link to **PrimeDesignArts** on Etsy: https://www.etsy.com/shop/PrimeDesignArts

# Link to **LetitiasArt** on Etsy: https://www.etsy.com/ca/shop/LetitiasArt

# Link to **DashaDesignStudio** on Etsy: https://www.etsy.com/shop/DeshadiaDesignStudio

# ##### Worth considering: #####
# Link to **FusionMM** on Etsy: https://www.etsy.com/shop/FusionMM

# ![FusionMM%20Etsy.png](attachment:FusionMM%20Etsy.png)

# ![FusionMM%20Products%20etsy.png](attachment:FusionMM%20Products%20etsy.png)

# Despite the difference in artistic style and product presentations, FusionMM is labelled as "Worth conisdering" for Chien-Chien given the vast selection of product offerings and the rich variety of the materials used. 

# ##### Worth considering: #####
# Link to **Coconuttowers** on Etsy: https://www.etsy.com/shop/Coconuttowers

# ![Coconuttowers%20etsy.png](attachment:Coconuttowers%20etsy.png)

# ![Coconuttowers%20Products%20etsy.png](attachment:Coconuttowers%20Products%20etsy.png)

# Similar to FusionMM's reason of inclusion, Coconuttowers is chosen thanks to its wide variety of painting subject (different animal portraits) and the different presentations of a similar theme. 

# Link to **veniceme** on Etsy: https://www.etsy.com/shop/veniceme

# ##### Worth considering: #####
# Link to **rainbowofcrazy** on Etsy: https://www.etsy.com/shop/rainbowofcrazy

# ![rainbowofcrazy%20etsy.png](attachment:rainbowofcrazy%20etsy.png)

# ![rainbowofcrazy%20Products%20etsy.png](attachment:rainbowofcrazy%20Products%20etsy.png)

# rainbowofcrazy, on the other hand, sells an even-wider selection of products while retaining its core product offering - animal-related illustration; Chien-Chien can aspire to utilize the same strategy of expanding its product presentation (such as using different materials or different printing style) while maintaining its unique selling point. 

# ### Conclusion for subcategory, 'Painting', in the main category, "Gift" ###

# It seems that all results from this subcategory belongs to customizable protraits of either dogs or people. The majority of the products belong in the "Pet Supplies" main category, while a minority of them goes towards "Art & Collectibles".

# ### Creating the dataframe for the subcategory, 'Paper', from the main category, "Gift".

# In[21]:


etsy_gift_paper = etsy_gift[etsy_gift['description'].str.contains('Paper')]
etsy_gift_paper


# In[22]:


etsy_gift_paper.info()


# In[23]:


etsy_gift_paper.describe()


# In[24]:


etsy_gift_paper_pricemean = 48.55
etsy_gift_paper_pricemean


# As the results have shown, there are 7 counts of returns that match our desired filter. The **mean is 48.55** and a **standard deviation of 50.85** for the "price" column. Similar to "etsy_gift_painting", this dataframe features drastic differences between products, with the most and least expensive item being **143.27** apart; the "reviews_count" also displays the same phenomenon. 
# 
# Below is a Bar Chart that showcases the difference of price between each brand visually. 

# In[25]:


# create a Bar Chart with each brand as X and price as Y
etsy_gift_paper_bar = alt.Chart(etsy_gift_paper).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    tooltip=['price']
    )

etsy_gift_paper_bar


# In[26]:


# Unique cateory in etsy_gift_paper
etsy_gift_paper_category = etsy_gift_paper['category'].unique().tolist()
etsy_gift_paper_category


# With the shift of search term, the corresponding catergories have also changed and expanded to include "Wedding" and "Clothing" as well. The seven products are quite evenly spaced out between the six categories when compared to "etsy_gift_painting".

# In[27]:


# sort value by average_rating
etsy_gift_paper_sort = etsy_gift_paper.sort_values(by=['average_rating'], ascending=False)
etsy_gift_paper_sort


# After sorting this dataframe through descending order by "average_rating", it's clear that **KolonjaArt is the highest rated brand on average with 359 review counts**; however, its review count is still significantly lower than the **mean of 2163.57** in comparison. 

# In[28]:


# Unique brand in etsy_gift_paper
etsy_gift_paper_brand = etsy_gift_paper['brand'].unique().tolist()
etsy_gift_paper_brand


# Link to **KolonjaArt** on Etsy: https://www.etsy.com/shop/KolonjaArt

# Link to **MyCrayonsDesign** on Etsy: https://www.etsy.com/shop/MyCrayonsDesign

# Link to **BlissPaperBoutique** on Etsy (currently NOT selling): https://www.etsy.com/shop/BlissPaperBoutique

# Link to **DreamyDressUps** on Etsy (currently NOT selling): https://www.etsy.com/shop/DreamyDressUps

# Link to **NadineSophieArt** on Etsy (deactivivated): n/a

# Link to **Paperealities** on Etsy: https://www.etsy.com/shop/Paperealities

# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# ### Conclusion for the subcategory, 'Paper', in the main category, "Gift" ###

# The 7 results seem to be split in two directions, "Wedding" and "Custom Portrait", with a great range of prices for portrait works and digital wedding templates/products.

# ### "Decor" Main Category

# In[29]:


etsy_decor = etsy[etsy['description'].str.contains('Decor')]
etsy_decor


# In[30]:


etsy_decor.info()


# In[31]:


etsy_decor.describe()


# Looking at the *.describe()* results, the **count shows 186 rows with a price mean of 64.76 and a price standard deivation of 71.77** overall. Much like the "Gift" main category, the dataframe will be filtered again with **Painting** and **Paper** as key search words in the "description" column. 

# ### Creating the dataframe for the subcategory of 'Painting' in the main category, "Decor". ###

# In[32]:


etsy_decor_painting = etsy_decor[etsy_decor['description'].str.contains('Painting')]
etsy_decor_painting


# In[33]:


etsy_decor_painting.info()


# In[34]:


etsy_decor_painting.describe()


# In[35]:


etsy_decor_painting_pricemean = 64.59
etsy_decor_painting_pricemean


# As shown in the results, this filtered dataframe contains **7 rows with a price mean of 64.59 and a price standard deviation of 40.39**. Unlike in the "Gift" main category, the min and max difference is less extreme, being **115** exact; the same can be said for "reviews_count". 
# 
# Below is a Bar Chart that viusally illustrates the difference of price between each brand. 

# In[36]:


# create a Bar Chart with each brand as X and price as Y
etsy_decor_painting_bar = alt.Chart(etsy_decor_painting).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    opacity=0.8,
    color='purple'
    )

etsy_decor_painting_bar


# In[37]:


# Unique cateory in etsy_decor_painting
etsy_decor_painting_category = etsy_decor_painting['category'].unique().tolist()
etsy_decor_painting_category


# The majority, 5 out of 7, seems to belong in the "Art & Colectibles" main category, while the remaining two items belong to the "Weddings" category. It seems that with the search term being "decor" first and "painting" second, the type of materials used differ substantially based on the sub-categories they belong in, including giclee, oil, gouache, and pencil. 

# In[38]:


# sort value by average_rating
etsy_decor_painting_sort = etsy_decor_painting.sort_values(by=['average_rating'], ascending=False)
etsy_decor_painting_sort


# Despite the low review counts, both **MARIARTpro and vteronikart are the highest rated sellers/brands on average**. Although the mean of "review_counts" sits at 150.43, the majority of brands actually only possess review counts below 3 figures, hence making that mean number a bit misleading; it is likely due to **LanreStudio and DigitalPrintsInc's 586 and 123 review counts respectively** that led to a high number for the mean.

# In[39]:


# Unique brand in etsy_decor_painting
etsy_decor_painting_brand = etsy_decor_painting['brand'].unique().tolist()
etsy_decor_painting_brand


# Link to **MARIARTpro** (currently NOT selling):
# https://www.etsy.com/shop/MARIARTpro

# Link to **vteronikart** (currently NOT selling):
# https://www.etsy.com/shop/vteronikart

# Link to **9028** from **DigitalPrintsInc**:
# https://www.etsy.com/listing/936395393/custom-portrait-from-photo-christmas

# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# Link to **4841** from **LanreStudio**:
# https://www.etsy.com/listing/509786885/english-bulldog-art-pet-portrait-animal

# Link to **LanreStudio** on Etsy: https://www.etsy.com/shop/LanreStudio

# Link to **CanvasGalery** (currently NOT selling):
# https://www.etsy.com/shop/CanvasGalery

# Link to **artsandcreations**: 
# https://www.etsy.com/shop/artsandcreations

# ### Conclusion for the subcategory, 'Painting', in the main category, "Decor" ###

# With many Etsy sellers/brands being self-proprietorships, half of the brands are no longer active on the platform as the time of this analysis. This dataframe, however, does seem to feature less extreme means and standard deviations in the quantitative columns, which signals to a more consistent price range and similar product offerings. 

# ### Creating the dataframe for the subcategory of 'Paper' in the main category, "Decor". ###

# In[40]:


etsy_decor_paper = etsy_decor[etsy_decor['description'].str.contains('Paper')]
etsy_decor_paper


# In[41]:


etsy_decor_paper.info()


# In[42]:


etsy_decor_paper.describe()


# In[43]:


etsy_decor_paper_pricemean = 23.20
etsy_decor_paper_pricemean


# Looking at the results above, the dataframe features more than double the amount of returns compared to "etsy_decor_painting", sitting at **15 rows with a price mean of 23.20 and a price standard deviation of 19.96**. Although the difference bewteen the most and least expensive product is no less substantial, **68.22**, it makes sense for this dataframe to have much lower price range since the filtered keywords are "decor" first and "paper" second. 
# 
# Below is a Bar Chart to visually illsutrate the difference in price between each brands (note: some brands sell multiple items in this dataframe, therefore the Bar Chart features a higher degree of contrast in opacity.)

# In[44]:


#create a Bar Chart with each brand as X and price as Y
etsy_decor_paper_bar = alt.Chart(etsy_decor_paper).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    color='purple'
    )

etsy_decor_paper_bar


# In[45]:


# Unique cateory in etsy_decor_paper
etsy_decor_paper_category = etsy_decor_paper['category'].unique().tolist()
etsy_decor_paper_category


# The great majority of the products, 14 out of 15 specifically, belong to the "Weddings" main category, with item **9028 from DigitalPrintsInc** belonging to "Art & Collectibles". Such a high degree of difference showcases the paper-decor needs for weddings. 

# In[46]:


# sort value by average_rating
etsy_decor_paper_sort = etsy_decor_paper.sort_values(by=['average_rating'], ascending=False)
etsy_decor_paper_sort


# Looking at the sorted dataframe, it's clear that **TheFoldingTreeStudio takes the crown for being the highest rated brand on average** despite the slightly meager review counts of 249; the **mean is 583.27** with HappyPartyDecor and LandofFlowers bringing that number higher when compared to other brands' reivew counts. 

# In[47]:


# Unique brand in etsy_decor_paper
etsy_decor_paper_brand = etsy_decor_paper['brand'].unique().tolist()
etsy_decor_paper_brand


# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# Link to **TheFoldingTreeStudio** on Etsy (taking a short break): https://www.etsy.com/shop/TheFoldingTreeStudio

# Link to **FlowerDecoration** on Etsy: https://www.etsy.com/shop/FlowerDecoration

# Link to **ArtdecorationByZhang** on Etsy (currently NOT selling): https://www.etsy.com/shop/ArtdecorationByZhang

# Link to **flower4you** on Etsy: https://www.etsy.com/shop/flower4you

# Link to **HappyPartyDecor** on Etsy (deactivated): n/a

# Link to **AdrianaOrtizDesigns** on Etsy: https://www.etsy.com/ca/shop/AdrianaOrtizDesigns

# Link to **LandofFlowers** on Etsy (currently NOT selling): https://www.etsy.com/shop/LandofFlowers

# ##### Worth considering: #####
# Link to **DreamEventsinPaper** on Etsy: https://www.etsy.com/shop/DreamEventsinPaper

# ![DreanEventsinPaper%20Etsy.png](attachment:DreanEventsinPaper%20Etsy.png)

# ![DreamEventsinPaper%20Product%20Etsy.png](attachment:DreamEventsinPaper%20Product%20Etsy.png)

# DreamEventsinPaper is a good consideration as its paper-centered products and the rich variety of presentations for the client's, Chien-Chien, e-commerce strategic direction.

# ### Conclusion for the subcategory, 'Paper', in the main category, "Decor" ###

# Factoring into the context of decoration products with paper materials, it is evident why the featured products more than double "etsy_decor_painting's" count and why the price range seems to be less signficant (since paper products are usually cheaper as paper is usually cheaper). With that said, the prices and review counts still differ quite a bit from one seller/brand to another, signalling a great fluctuation of pricing strategies in this dataframe.

# ### Creating the "Chinese" dataframe from the "Etsy" main dataframe

# In[48]:


# find Chinese in description
etsy_chinese = etsy[etsy['description'].str.contains('Chinese')]
etsy_chinese


# In[49]:


etsy_chinese.info()


# In[50]:


etsy_chinese.describe()


# In[51]:


etsy_chinese_pricemean = 49.16
etsy_chinese_pricemean


# Looking at the results, this dataframe features **23 rows with a price mean of 49.16 and a price standard deviation of 39.51**. The difference between the most and least expensive products are very signifacnt, as that number sits at **161.80**; an even more significant difference can be seen in "reviews_count", as the minimum value in that column is 1 and the maximum value is 2085, which equates to a staggering **difference between min & max for 2084!**
# 
# Below is a Bar Chart visually illustrating the differene in price between each seller/brand.

# In[52]:


# create a Bar Chart with each brand as X and price as Y
etsy_chinese_bar = alt.Chart(etsy_chinese).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    color='purple'
    )

etsy_chinese_bar


# In[53]:


# Unique cateory in etsy_chinese
etsy_chinese_category = etsy_chinese['category'].unique().tolist()
etsy_chinese_category


# While the majority of products still fall into the "Weddings" and "Art & Collectibles" main categories, the minority of them belong to a new category unseen before in this analysis - "Shoes", specifically "Unisex Kids' Shoes". Even within the broader umbrella of "Weddings", the variety of sub-categories differ quite a bit, including neckties, hair pins, umbrellas, etc. It is evident that, on Etsy, there are quite a few "Chinese" products across many categories. 

# In[54]:


# sort value by average_rating
etsy_chinese_sort = etsy_chinese.sort_values(by=['average_rating'], ascending=False)
etsy_chinese_sort


# Despite **NDArtShopDigital** sharing the crown with numerous other sellers/brands as the highest rated on average, its **single, 1, review** that gave it five out of five is very concerning and potentially fake (as some stores/e-commerce brands can feature fake reviews to boost their legitimacy); given that reason, I'm excluding it from the top spots. The following lists all obtained five out of five reviews with varying degree of review counts: **"designAnn, PatteLaisseDesTraces, TaoTaoHandWork, GoddessaDesires, and Louyingscrafts"**. 

# In[55]:


# Unique brand in etsy_chinese
etsy_chinese_brand = etsy_chinese['brand'].unique().tolist()
etsy_chinese_brand


# ##### Worth considering: (please view the screenshots and reason from above) #####
# Link to **DreamEventsinPaper** on Etsy: https://www.etsy.com/shop/accessories482

# Link to **BuyMeNowShop** on Etsy (currently NOT selling): https://www.etsy.com/shop/BuyMeNowShop

# ##### Worth considering:. #####
# Link to **PatteLaisseDesTraces** on Etsy: https://www.etsy.com/shop/PatteLaisseDesTraces

# ![PatteLaisseDesTraces%20Etsy.png](attachment:PatteLaisseDesTraces%20Etsy.png)

# PatteLaisseDesTraces focuses on illustratuons and prints on textured paper for its product offerings. Unfortunately, during the assembly of this analysis, all of their items have been taken of their storefront; therefore, I am unable to include any screenshots of their products nor product categories. Given the client's, Chien-Chien, focus on illustration and paper-related product, PatteLaisseDesTraces serves as a good inspiration.

# Link to **GoddessaDesires** on Etsy (deactivated): n/a

# ##### Worth considering:. #####
# Link to **Louyingscrafts** on Etsy: https://www.etsy.com/ca/shop/Louyingscrafts?ref=shop-header-name&listing_id=286515061&from_page=listing

# ![Louyingscrafts%20Etsy.png](attachment:Louyingscrafts%20Etsy.png)

# Louyingscrafts sells exclusively Chinese-related products, although mainly shoes for infants and kids. The reason why this seller can be a worthwhile consideration for inspiration is because of their focus on solely Asian-heritage-related products and printing/transposing their work onto available materials, such as shows and pillow cases. 

# Link to **SilkScarvesTakuyo** on Etsy: https://www.etsy.com/shop/SilkScarvesTakuyo

# Link to **TaoTaoHandWork** on Etsy (deactivated): n/a

# ##### Worth considering:. #####
# Link to **designAnn** on Etsy: https://www.etsy.com/shop/designAnn

# ![designAnn%20Etsy.png](attachment:designAnn%20Etsy.png)

# designAnn, seemingly being a self-proprietor shop on Etsy, serves as a good inspiration for the client as they also would be selling their own artworks in various mediums/using different materials. Although designAnn's products are more widespread in terms of her style, Chien-Chien can also divest and diversify its product offerings and style in a similar fashion.

# Link to **ChinaDesigner** on Etsy (currently NOT selling): https://www.etsy.com/shop/ChinaDesigner

# Link to **NDArtShop** on Etsy: https://www.etsy.com/shop/NDArtistShop?ref=nla_sfs

# ### Conclusion for "Chinese" dataframe in "Etsy"

# While Etsy's sellers and purchasers are predominatly based in North America and Europe, it is still encouraging to see sellers/brands utilizing Asian-styles to enrich their product offerings and the diversity of items on the platform. Despite some of the products being a direct replica/creation of Asian heritage, such as traditional Chinese shoes for kids from Louyingscrafts and Japanese kimono from SilkScarvesTakuyo, **the lack of Asian-styles of artwork presented through a more traditionally Western medium, like Chinese caligraphy on handmade paper, signals an opportunity for Chien-Chien to insert itself into this e-commerce market.**

# ### Creating the "Japanese" dataframe from the "Etsy" main dataframe

# In[56]:


# Find Japanese in description
etsy_japanese = etsy[etsy['description'].str.contains('Japanese')]
etsy_japanese


# In[57]:


etsy_japanese.info()


# In[58]:


etsy_japanese.describe()


# In[59]:


etsy_japanese_pricemean = 109.86
etsy_japanese_pricemean


# The "Japanese" dataframe features **34 rows with a price mean of 109.86 and a price standard deviation of 149.88**. The difference between the most and least expensive is the most staggering number, thus far, in the analysis, sitting at a towering **701.95**; this signals a very significant difference in pricing for "etsy_japanese"; same can be said for "reviews_count" as its difference between min & max sits at a whopping **20840**. 
# 
# Below is a Bar Chart that illustrates the difference in prices between each brand visually.

# In[60]:


# create a Bar Chart with each brand as X and price as Y
etsy_japanese_bar = alt.Chart(etsy_japanese).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    color='purple'
    )

etsy_japanese_bar


# While most brands selling "Japanese"-related products under the thrusthold of $100, some greatly exceed that bar. Although a few of the most expensive products can perhaps be eliminated from the "etsy_japanese" dataframe, due to them being potential outliers, such a decision may compromise the integrity of the data set and mislead the direction or conclusion of the analysis. Therefore, all data entries will be kept as is.

# In[61]:


# Unique cateory in esty_japanese
etsy_japanese_category = etsy_japanese['category'].unique().tolist()
etsy_japanese_category


# The "Japanese" products spam across an even wider array of categories than "Chinese", with the addition of "Toys & Games" to the mix of "Weddings", "Pet Supplies", "Art & Collectibles" and "Shoes < Unisex Kids' Shoes". The subcategories of "Weddings" specifically are even more expansive, ranging from "Shawls & Wraps" to "Bouquets". Such a wide selection of categories make sense when factoring the idea that "Japanese" can also be referred to as a style instead of place of manufacturing. 

# In[62]:


# sort value by average_rating
etsy_japanese_sort = etsy_japanese.sort_values(by=['average_rating'], ascending=False)
etsy_japanese_sort


# When it comes to the highest rated sellers/brands on average, the list is quite expansive, as well; there are many with varying numbers of review counts. **The Etsy customerbase seems to be quite content overall with "Japanese"-related products with a high mean of 4.93 for "average_rating" and 1004.44 for "reviews_count".**

# In[63]:


# Unique brand in etsy_japanese
etsy_japanese_brand = etsy_japanese['brand'].unique().tolist()
etsy_japanese_brand


# Link to **SilkScarvesTakuyo** on Etsy: https://www.etsy.com/shop/SilkScarvesTakuyo

# ##### Worth considering (please visit the screenshot and comment from above) #####
# Link to **designAnn** on Etsy: https://www.etsy.com/shop/designAnn

# Link to **KathleenBarryJewelry** on Etsy: https://www.etsy.com/shop/KathleenBarryJewelry

# Link to **Dodero** on Etsy (currently NOT selling): https://www.etsy.com/shop/Dodero

# Link to **MagicRibbonByMira** on Etsy: https://www.etsy.com/shop/MagicRibbonByMira

# Link to **NeoNeonStudioPrint** on Etsy: https://www.etsy.com/shop/NeoNeonStudioPrint

# Link to **ByFlowerIndulgence** on Etsy (currently NOT selling): https://www.etsy.com/shop/ByFlowerIndulgence

# Link to **GoldenHornOutdoor** on Etsy: https://www.etsy.com/shop/GoldenHornOutdoor

# Link to **RedHillPrintables** on Etsy: https://www.etsy.com/shop/RedHillPrintables

# Link to **MollyAngie** on Etsy: https://www.etsy.com/shop/MollyAngie

# Link to **LuxuriaFata** on Etsy (deactivated): n/a

# Link to **SunLondon** on Etsy: https://www.etsy.com/shop/SunLondon

# ##### Worth considering: #####
# Link to **FawnandFloDesigns** on Etsy: https://www.etsy.com/shop/FawnAndFlo

# ![FawnandFloDesigns%20Etsy.png](attachment:FawnandFloDesigns%20Etsy.png)

# ![FawnandFloDesigns%20Product%20Etsy.png](attachment:FawnandFloDesigns%20Product%20Etsy.png)

# FawnandFlo (previously named FawnandFloDesigns) is a great inspiration for the client's strategic direction and product offerings; the shop being a self-proprietorship and offers a wide selection of illustration-or-paper-based items through various mediums (like mugs and phone cases). 

# Link to **SaisonRomantique** on Etsy (currently NOT selling): https://www.etsy.com/fr/shop/SaisonRomantique

# Link to **veniceme** on Etsy: https://www.etsy.com/shop/veniceme

# Link to **TwoCatsAndAnOwl** on Etsy: https://www.etsy.com/shop/TwoCatsAndAnOwl

# Link to **LIFEHONEY** on Etsy: https://www.etsy.com/shop/LIFEHONEY

# ##### Worth considering: #####
# Link to **PresentPerfectStudio** on Etsy: https://www.etsy.com/shop/PresentPerfectStudio

# ![PresentPerfectStudio%20Etsy.png](attachment:PresentPerfectStudio%20Etsy.png)

# ![PresentPerfectStudio%20Product%20Etsy.png](attachment:PresentPerfectStudio%20Product%20Etsy.png)

# PresentPerfectStudio, being another self-proprietorship and flower-focused shop, is a great conisderation for Chien-Chien as well, since the client wishes to incorporate "flowers" in many of their illustrations and product offerings. The wide selection of flower-related products can be a source of inspiration as well. 

# Link to **Rakuchin** on Etsy: https://www.etsy.com/shop/Rakuchin

# Link to **Cyberoptix** on Etsy: https://www.etsy.com/shop/Cyberoptix

# Link to **omoonwood** on Etsy (currently NOT selling): https://www.etsy.com/shop/omoonwood

# Link to **ValkyriaCreations** on Etsy: https://www.etsy.com/shop/ValkyriaCreations

# Link to **EdenLuxeBridal** on Etsy: https://www.etsy.com/shop/EdenLuxeBridal

# Link to **AoiClothingFR** on Etsy (currently NOT selling): https://www.etsy.com/shop/AoiClothingFR

# Link to **Rozenhandmade** on Etsy: https://www.etsy.com/shop/Rozenhandmade

# Link to **DebbieCarlisleLtd** on Etsy: https://www.etsy.com/shop/DebbieCarlisleLtd

# Link to **Tatishotties** on Etsy (currently NOT selling): https://www.etsy.com/shop/Tatishotties

# ### Conclusion for "Japanese" dataframe from "Esty"

# The "Japanese" dataframe includes a vast array of products under a wide range of categories. Despite the significant difference of pricing and review counts, this dataframe showcases an appetite for Asian-related products in a predominantly North American and European market on Etsy. In particular, FawnandFlo and PresentPerfectStudio serve as great inspirations for the client to tailor their business strategy and production pipelines around. 

# ### "Custom" Main Category

# In[64]:


# Find custom in description
etsy_custom = etsy[etsy['description'].str.contains('Custom')]
etsy_custom


# In[65]:


etsy_custom.info()


# In[66]:


etsy_custom.describe()


# Looking at the results, it seems that Etsy has a large amount of sellers/brands that offer customizable products. However, it is absolutely necessary to break this down further into **Painting** and **Paper** subcategories to better assess the data set and match the client's needs/direction. 

# ### Creating the dataframe for the subcategory of 'Painting' in the main category, "Custom". ###

# In[67]:


# etsy_custom_painting
etsy_custom_painting = etsy_custom[etsy_custom['description'].str.contains('Painting')]
etsy_custom_painting


# In[68]:


etsy_custom_painting.info()


# In[69]:


etsy_custom_painting.describe()


# In[70]:


etsy_custom_painting_pricemean = 68.56
etsy_custom_painting_pricemean


# Based on the results, this dataframe returns **34 rows with a price mean of 68.56 and a price standard deviation of 53.84**. Factoring in the context of each artist/seller charging different prices for their artwork, it makes sense that there is a huge disparity, of **230.44** between the least and most expensive products within "etsy_custom_painting"; the "reviews_count" column also shares a very similar characteristic, with a whopping **4535** difference. 
# 
# Below is a Bar Chart illustrating the difference of prices between each brand visually.

# In[71]:


# create a Bar Chart with each brand as X and price as Y
etsy_custom_painting_bar = alt.Chart(etsy_custom_painting).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    )

etsy_custom_painting_bar


# As shown in the graph, most sellers/brands keep their prices below the $60 range; however, **LetitiasArt & svetlanamatevosjan** are the two highest priced brands within this dataframe, thus bringing the mean value a lot higher as a result. 

# In[72]:


# Unique cateory in etsy_custom_painting
etsy_custom_painting_category = etsy_custom_painting['category'].unique().tolist()
etsy_custom_painting_category


# With the key search word being "Painting", the results of unique categories are unsurprising, as "Art & Collectibles" and "Pet Portraits" take the crown for housing most of the products. "Weddings" trail behind as the third most common category in this dataframe.

# In[73]:


# sort value by average_rating
etsy_custom_painting_sort = etsy_custom_painting.sort_values(by=['average_rating'], ascending=False)
etsy_custom_painting_sort


# Quite a few sellers/brands achieved a 5 out of 5 review on average, despite their review counts being substantially lower than the ones with high review counts that exceed even four figures; the top rated sellers/brands include **breadandjaim, LetitiasArt, vteronikart, CustomArtsFromDavid, Coconuttowers, DashaDesignStudio, LITDigitalPaintings, and svetlanamatevosjan**.

# In[74]:


# Unique brand in etsy_custom_painting
etsy_custom_painting_brand = etsy_custom_painting['brand'].unique().tolist()
etsy_custom_painting_brand


# ##### Worth considering: #####
# Link to **breadandjaim** on Etsy: https://www.etsy.com/shop/cottonandbowpaper

# ![breadandjaim%20Etsy.png](attachment:breadandjaim%20Etsy.png)

# ![breadandjaim%20Product%20Etsy.png](attachment:breadandjaim%20Product%20Etsy.png)

# Cottonandbow (previously named "breadandjaim") focuses a lot of paper-based products with customizable lettering, caligraphy and illustrations; this attribute, combined with a huge variety of product selections, makes for a good inspiration for the client to model their e-commerce store after. 

# Link to **ThatMomentPortraits** on Etsy: https://www.etsy.com/shop/ThatMomentPortraits?ref=simple-shop-header-name&listing_id=1273673095

# Link to **LetitiasArt** on Etsy: https://www.etsy.com/ca/shop/LetitiasArt

# ##### Worth considering: #####
# Link to **svetlanamatevosjan** on Etsy: https://www.etsy.com/shop/svetlanamatevosjan

# ![svetlanamatevosjan%20Etsy.png](attachment:svetlanamatevosjan%20Etsy.png)

# ![svetlanamatevosjan%20Product%20Etsy.png](attachment:svetlanamatevosjan%20Product%20Etsy.png)

# svetlanamatevosjan is a self-propreitor online storefront with a focus on customizable/commission-based paintings and drawings.  The artist-led direction and huge product variety make this seller/brand a good example for Chien-Chien to model itself after, thus making svetlanamatevosjan a worthy consideration.

# Link to **MicromysWatercolor** on Etsy (currently not selling): https://www.etsy.com/shop/MicromysWatercolor

# ##### Worth considering: #####
# Link to **studiotuesday** on Etsy: https://www.etsy.com/shop/studiotuesday

# ![studiotuesday%20Etsy.png](attachment:studiotuesday%20Etsy.png)

# ![studiotuesday%20Product%20Etsy.png](attachment:studiotuesday%20Product%20Etsy.png)

# studiotuesday makes for a good inspiration thanks to its illustrations (primarily Watercolors) and its foucs on animal/pet portraits. The client can model their digital storefront in a similar fashion, such as using different materials to present their artworks with a common theme across the board. 

# Link to **PrimeDesignArts** on Etsy: https://www.etsy.com/shop/PrimeDesignArts

# Link to **CustomArtsFromDavid** on Etsy (currently not selling): https://www.etsy.com/shop/CustomArtsFromDavid

# Link to **lumetri** on Etsy: https://www.etsy.com/shop/lumetri

# Link to **NadineSophieArt** on Etsy (deactivivated): n/a

# Link to **DesignMyDog** on Etsy (currently not selling): https://www.etsy.com/shop/DesignMyDog

# Link to **DashaDesignStudio** on Etsy: https://www.etsy.com/shop/BabylonBazaArt

# Link to **LITDigitalPaintings** (deactivated): n/a

# ##### Worth considering (please visit the screenshots and comment from above) #####
# Link to **FusionMM** on Etsy: https://www.etsy.com/shop/FusionMM

# ##### Worth considering (please visit the screenshots and comment from above) #####
# Link to **Coconuttowers** on Etsy: https://www.etsy.com/shop/Coconuttowers

# Link to **veniceme** on Etsy: https://www.etsy.com/shop/veniceme

# Link to **VyaArt** on Etsy (currently not selling): https://www.etsy.com/shop/VyaArt

# Link to **vteronikart** (currently NOT selling):
# https://www.etsy.com/shop/vteronikart

# ##### Worth considering (please visit the screenshots and comment from above) #####
# Link to **rainbowofcrazy** on Etsy: https://www.etsy.com/shop/rainbowofcrazy

# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# ##### Worth considering: #####
# Link to **MaryArtStudio** on Etsy: https://www.etsy.com/shop/MaryArtStudio

# ![MaryArtStudio%20Etsy.png](attachment:MaryArtStudio%20Etsy.png)

# ![MaryArtStudio%20Product%20Etsy.png](attachment:MaryArtStudio%20Product%20Etsy.png)

# MaryArtStudio focuses on customizable line and Watercolors drawings with some products being digital only; the client can model its product offerings in a similar fashion for their online brand.

# Link to **DanasPaperFlowers** on Etsy: https://www.etsy.com/shop/DanasPaperFlowers

# ### Conclusion for the subcategory, 'Painting', in the main category, "Custom" ###

# Despite the high degree of variation in its pricing and review counts, this dataframe has provided some good examples for the client to model their own e-commerce brand after, as some sellers/brands have captured their own niche audience through a very clear focus on their style and product offerings, such as animal/pet-themed Watercolors paintings or customizable line art. 

# ### Creating the dataframe for the subcategory of 'Paper' in the main category, "Custom". ###

# In[75]:


# etsy_custom_paper
etsy_custom_paper = etsy_custom[etsy_custom['description'].str.contains('Paper')]
etsy_custom_paper


# In[76]:


etsy_custom_paper.info()


# In[77]:


etsy_custom_paper.describe()


# In[78]:


etsy_custom_paper_pricemean = 48.40
etsy_custom_paper_pricemean


# Looking at the results, this dataframe includes **25 rows with a price mean of 48.40 and a price standard deivation of 60.66**. Similar to "etsy_custom_painting", this one also shares a huge disparity between the least and most expensive products of **269.01**; the "reviews_count" column shows an even-more significant difference of **3071**! Factoring the context of artists pricing their artwork very differently, this big margin of difference seems to be reasonable.  
# 
# Below is a Bar Chart that illustrates the difference in prices between each seller/brand.

# In[79]:


# create a Bar Chart with each brand as X and price as Y
etsy_custom_paper_bar = alt.Chart(etsy_custom_paper).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    ).configure_mark(
    color='purple'
    )

etsy_custom_paper_bar


# As shown in the graph, the majority of brands have listed their products under the price range of 50. Three sellers, however, chose to price their work above the $150 line, including **HAPPYprojectSHOP, NadineSophieArt, and DanasPaperFlowers**; this explains the high value of the price mean in this dataframe. 

# In[80]:


# Unique cateory in etsy_custom_paper
etsy_custom_paper_category = etsy_custom_paper['category'].unique().tolist()
etsy_custom_paper_category


# There seems to be a more even distribution of categories among this dataframe, as "Weddings", "Art & Collectibles" and "Pet Portraits", once again, encompass all the products. Despite the key search word being "Paper", the dataframe seems to also include "Digital/Digital Prints" in its subcatergories, which may explain the lower price points, as digital art printed on paper is likely cheaper than handcrafted arts directed painted on canvas. 

# In[81]:


# sort value by average_rating
etsy_custom_paper_sort = etsy_custom_paper.sort_values(by=['average_rating'], ascending=False)
etsy_custom_paper_sort


# Three sellers/brands take the crown as **the highest rated on average, including TheFoldingTreeStudio, KolonjaArt, and Portraitofmypets**; the last seller only has 7 reviews, which hinders their credibility. 

# In[82]:


# Unique brand in etsy_custom_paper
etsy_custom_paper = etsy_custom_paper['brand'].unique().tolist()
etsy_custom_paper


# Link to **TheFoldingTreeStudio** on Etsy: https://www.etsy.com/shop/TheFoldingTreeStudio

# Link to **NadineSophieArt** on Etsy (deactivivated): n/a

# ##### Worth considering (please visit the screenshots and comment from above) #####
# Link to **DreamEventsinPaper** on Etsy: https://www.etsy.com/shop/accessories482

# Link to **DigitalPrintsInc** on Etsy: https://www.etsy.com/shop/DigitalPrintsInc

# Link to **Portraitofmypets** on Etsy: https://www.etsy.com/uk/shop/PortraitofMyPet

# Link to **ThatMomentPortraits** on Etsy: https://www.etsy.com/shop/ThatMomentPortraits?ref=simple-shop-header-name&listing_id=1273673095

# Link to **KolonjaArt** on Etsy: https://www.etsy.com/shop/KolonjaArt

# Link to **SmittenPaperProps** on Etsy (currently NOT selling): https://www.etsy.com/shop/SmittenPaperProps

# Link to **HAPPYprojectSHOP** on Etsy: https://www.etsy.com/shop/HAPPYprojectSHOP

# ##### Worth considering: #####
# Link to **FioriBelle** on Etsy: https://www.etsy.com/shop/FioriBelle

# ![FioriBelle%20Etsy.png](attachment:FioriBelle%20Etsy.png)

# ![FioriBelle%20Product%20Etsy.png](attachment:FioriBelle%20Product%20Etsy.png)

# FioriBelle makes for a suitable candidate to model the client's e-commerce brand after, as their vast collection of illustration-based products, such as pins, cards, and stickers, provide a good template for Chien-Chien's product offerings. 

# Link to **LandofFlowers** on Etsy (currently NOT selling): https://www.etsy.com/shop/LandofFlowers

# Link to **PixelAndPaperPets** on Etsy: https://www.etsy.com/shop/PixelAndPaperPets

# Link to **DanasPaperFlowers** on Etsy: https://www.etsy.com/shop/DanasPaperFlowers

# Link to **Paperealities** on Etsy: https://www.etsy.com/shop/Paperealities

# Link to **Filterity** on Etsy: https://www.etsy.com/shop/Filterity

# ### Conclusion for the subcategory, 'Paper', in the main category, "Custom" ###

# It is clear that for products that are customizable by nature, they tend to mostly fall under the "Wedding", "Art & Collectibles" categories, with a few being "Pet Portraits". Through the suitable inspirations, **FioriBelle and DreamEventsinPaper** serve as the best match for the client's needs and direction. 

# ### Creating the "Color Print" dataframe from the "Etsy" main dataframe

# In[84]:


# search color print in etsy
etsy_color_print = etsy[etsy['description'].str.contains('color print')]
etsy_color_print


# In[85]:


etsy_color_print.info()


# In[86]:


etsy_color_print.describe()


# In[87]:


etsy_color_print_pricemean = 42.57
etsy_color_print_pricemean


# This dataframe returns only **9 rows with a price mean of 42.57 and a price standard deviation of 44.33**. The difference between the least and most expensive item seems noticable, with **the difference being 129.05**; a similar phenomenon can be observed in the "reviews_count" column as the disparity is even bigger, sitting at **5301**! 
# 
# The Bar Chart below illustrates the difference in prices between each seller/brand.

# In[88]:


# create a Bar Chart with each brand as X and price as Y
etsy_color_print_bar = alt.Chart(etsy_color_print).mark_bar().encode(
    alt.X('brand'),
    alt.Y('price', stack=False),
    alt.Opacity('count()'),
    tooltip=['price', 'count()']
    )

etsy_color_print_bar


# Looking at the graph, it is clear that three sellers, **ilaStrate, SparkArtwork, and BreezyBirdGoodies**, caused the mean to be a lot higher than the average price of the majority of items; 6 out of 9 sit at around the $20 range. 

# In[89]:


# Unique cateory in etsy_color_print
etsy_color_print_category = etsy_color_print['category'].unique().tolist()
etsy_color_print_category


# Surprisingly, this dataframe features an unusual category - "Toys & Games < Yoga"; putting that oddity aside, other categories make a lot of sense given the context of "Color Prints". 

# In[90]:


# sort value by average_rating
etsy_color_print_sort = etsy_color_print.sort_values(by=['average_rating'], ascending=False)
etsy_color_print_sort


# Out of all sellers, three take the crown as the **highest rated on average, including ilaStrate, BalanceUA, and JasperAndRuby**; the last one is perhaps the most credible as their review count sits at a very comfortable spot of 747. 

# In[91]:


# Unique brand in etsy_color_print
etsy_color_print_brand = etsy_color_print['brand'].unique().tolist()
etsy_color_print_brand


# Link to **thepaperedwedding** on Etsy: https://www.etsy.com/shop/thepaperedwedding

# Link to **BreezyBirdStudio** on Etsy (taking a short break): https://www.etsy.com/uk/shop/BreezyBirdGoodies?ref=shop-header-name&listing_id=585583517&from_page=listing

# Link to **ilaStrate** on Etsy: https://www.etsy.com/shop/ilaStrate

# ##### Worth considering: #####
# Link to **JasperAndRuby** on Etsy: https://www.etsy.com/shop/JasperAndRuby

# ![JasperAndRuby%20Etsy.png](attachment:JasperAndRuby%20Etsy.png)

# ![JasperAndRuby%20Product%20Etsy.png](attachment:JasperAndRuby%20Product%20Etsy.png)

# JasperAndRuby serves as a good model to imitate thanks to its heavy emphasis on a common theme for illustrations (i.e., dogs) and the large variety of products available across different mediums, such as keychains, mugs, digital downloads, blankets, etc.

# Link to **SparkArtwork** on Etsy: https://www.etsy.com/shop/SparkArtwork

# Link to **JustLovelyPaintings** on Etsy (currently not selling): https://www.etsy.com/uk/shop/JustLovelyPaintings

# Link to **YourLUMADesign** on Etsy: https://www.etsy.com/shop/YourLUMADesign

# ##### Worth considering: #####
# Link to **BalanceUA** on Etsy: https://www.etsy.com/shop/BalanceUA

# ![BalanceUA%20Etsy.png](attachment:BalanceUA%20Etsy.png)

# ![BalanceUA%20Product%20Etsy.png](attachment:BalanceUA%20Product%20Etsy.png)

# BalanceUA focuses a lot on clip arts done with different styles and techniques (i.e., Watercolors, line art, etc.) and artwork prints of different kinds; this is also a suitable candidate for the client to model their e-commerce store and product offerings after.

# ### Conclusion for "Color Print" dataframe from "Esty"

# Despite the limited entries, this dataframe still provided a valuable insights into what kind of products and categories that may feature the key words of "Color Print" in them. Out of all sellers, **JasperAndRuby and BalanceUA** serve as good examples for Chien-Chien to model their strategic direction after.

# ### Creating the "Handmade Paper" dataframe from the "Etsy" main dataframe

# In[92]:


# etsy_handmade_paper = find "handmade paper" in "product_details"
etsy_handmade_paper = etsy[etsy['product_details'].str.contains('handmade paper')]
etsy_handmade_paper


# In[93]:


etsy_handmade_paper_price = 23
etsy_handmade_paper_price


# Link to **10145 by LineAveCalligraphy** on Etsy: https://www.etsy.com/listing/666501658/monthly-milestone-cards-watercolor-bow

# ![Handmade%20Paper%20Product%20Etsy.png](attachment:Handmade%20Paper%20Product%20Etsy.png)

# As the dataframe only returned one result, it is evident that there is a lack of competition in the "Handmade Paper" type of products. Given its **315 postive reviews**, an appeitite for this kind of artwork is definitely an unexplored blue ocean for the client.

# Link to **LineAveCalligraphy** on Etsy: https://www.etsy.com/shop/LineAveCalligraphy?ref=shop-header-name&listing_id=666501658&from_page=listing

# ![LineAveCalligraphy%20Etsy.png](attachment:LineAveCalligraphy%20Etsy.png)

# ![LineAveCalligraphy%20Product%20Etsy.png](attachment:LineAveCalligraphy%20Product%20Etsy.png)

# Putting aside the more Western-style of artwork, **LineAveCalligraphy** serves as a fantastic inspiration for the client as their empahsis on calligraphy and different kinds of print materials (i.e., handmade paper, digital, etc.) mark a huge differentiation from other artist-led, self-proprietorship Etsy brands. Chien-Chien can utilize similar product offerings and variety with a different focus on Eastern/Asian art style. 

# ## Data Analysis Conclusion

# Despite the data set being slightly outdated from 2021, the insights that are derived from it is still useful in giving the client a glimpse into the global market and relevant product offerings on the Etsy e-commerce platform. There are many sellers that share similar traits with Chien-Chien, and many of those brands have been highlighted accordingly that can help the client to more appropriately tailor their own online shop on Etsy after. Based on the results from this analysis, there seems to lie **a vacancy of Asian-style artworks with customizable options for both its artwork/written text (i.e., animal, calligraphy, etc.) and used materials (i.e., color print, digital, handmade paper, etc.)**; it is pivotal for the client to take advantage of this opportunity and quickly establish an online presence on Etsy and other social media sites (like many other sellers/brands). 

# ### Total Mean of Price

# In[102]:


Cobined_pricemean = (
                     etsy_gift_painting_pricemean 
                     + etsy_gift_paper_pricemean 
                     + etsy_decor_painting_pricemean 
                     + etsy_decor_paper_pricemean 
                     + etsy_chinese_pricemean 
                     + etsy_japanese_pricemean 
                     + etsy_custom_painting_pricemean 
                     + etsy_custom_paper_pricemean 
                     + etsy_color_print_pricemean 
                     + etsy_handmade_paper_price
                    )
    
Total_pricemean = Cobined_pricemean / 10

Total_pricemean


# The **total mean of price overall, combining all of the means of the relevant products and their prices and dividing them, is $57.376**; this serves as a good bench mark of the overall average price for similar products. 

# ## SWOT Analysis

# #### Strengths
# 1. Unique blend of Asian artworks/calligraphy with Western materials.
# 2. Cheaper material costs in comparison (i.e., Taiwanese vs. North American prices). 

# #### Weaknesses
# 1. Self-proprietorship (i.e., one artist only) limits the production and operational efficiency. 
# 2. International shipping fees (i.e., from Taiwan to North America) may deter purchases. 

# #### Opportunities
# 1. Lack of products featuring Asian-style artworks or calligraphy.
# 2. Lack of customizable handmade paper artworks/letters. 

# #### Threats
# 1. Market saturation with an abundance of "Paper" products on Etsy already.
# 2. Logistical concerns of shipping (i.e., package lost/damaged, etc.) and post-purchase customer service (i.e., refund or package returns, etc.).

# ![%E5%8D%83%E5%8D%83%E4%B9%8B%E7%BE%8E%20-%20SWOT%20Analysis.png](attachment:%E5%8D%83%E5%8D%83%E4%B9%8B%E7%BE%8E%20-%20SWOT%20Analysis.png)

# Analysis Compiled and Executed by **Max Chen**
# 
# Last Updated on: **March 30th 2025**
