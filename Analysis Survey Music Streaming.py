#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


inpPath = "C:/CarolineZiegler/Studium_DCU/7. Semester/Business Strategy/"
BS_Df = pd.read_csv(inpPath + "Music Streaming Survey Raw Data.csv", delimiter = ",")
BS_Df


# In[3]:


#The survey was conducted using Google Forms, which means that questions with a selection can already be evaluated very well in Google Forms. In this respect, Python is mainly used to clean the data, extract the customers and non-customers data sets and analyze the free-form texts. Consequently, not every column of the data set was analyzed in Python, but the gaps from Google Forms were filled by Python. 


# In[4]:


BS_Df.drop("Timestamp", inplace = True, axis =1)
BS_Df


# In[5]:


BS_Df.columns


# In[6]:


BS_Df.rename(columns = {"What is your gender?": "Gender", 
                        "What is your age group?":"Age Group", 
                        "What is your Country of Residence?": "Residence", 
                        "Are you subscribed to a music streaming platform?":"Music Streaming Subscription", 
                        "Why do you not use music streaming? (multiple answers possible)":"Reasons Non-Customers", 
                        "Which channels do you use instead? (you can finish this survey after this question)":"Music Listening by Non-Customers", 
                        "Which platform do you use mainly?":"Music Streaming Platform", 
                        "Why do you use this platform?":"Reasons for Platform",
                        "How often do you use music streaming?": "Music Streaming Frequency",
                        "Which subscription model do you use?":"Subscription Model",
                        "On which devices do you use music streaming services?": "Music Streaming Devices",
                        "When do you use music streaming services?": "Music Streaming Occasions",
                        "How satisfied are you with your current music streaming platform?": "Platform Satisfaction",
                        "I am satisfied, because...": "Reasons for Satisfaction",
                        "I am not satisfied, because...": "Reasons for Dissatisfaction",
                        "Which of the following interfaces do you find most appealing?": "Interface Appeal",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [High-quality audio ]": "High-quality Audio",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Cross-Platform Syncing ]": "Cross-Platform Syncing",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Shared Playlists ]": "Shared Playlists",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Live Lyrics Integration]": "Live Lyrics Integration",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Smart Speaker Integration]": "Smart Speaker Integration",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Concert & Event Integration]": "Concert & Event Integration",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Podcast]": "Podcast",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Offline Mode]": "Offline Mode",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Live Streaming Events]": "Live Streaming Events",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Sleep Timer]": "Sleep Timer",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Genre-Based Radio Stations ]": "Genre-Based Radio Stations",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Music Videos]": "Music Videos",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Personalized Recommendations]": "Personalized Recommendations", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Vast Music Library]":"Vast Music Library", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Exact Search and Discovery]":"Exact Search and Discovery", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Enhanced Artist Pages (e.g., biography)]":"Enhances Artist Pages", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [User Reviews and Ratings]":"User Reviews and Ratings", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Launch A Mix Inspired By A Song You Love]":"Launch a Mix", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Change Your Country Recommendations ]":"Change Country Recommendations", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Flow (moods, genres) ]":"Flow", 
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Song catcher (tracks and/or humming)]":"Song Catcher",
                        "What do you consider must-have, nice-to-have features on a music streaming platform and what do you personally not need? [Music Quizz ]": "Music Quiz"}, inplace = True)
BS_Df


# In[7]:


BS_Df["Interface Appeal"]


# In[8]:


BS_Df["Residence"].unique()


# In[9]:


BS_Df["Residence"] = BS_Df["Residence"].str.capitalize()
BS_Df["Residence"].unique()


# In[10]:


BS_Df["Residence"].replace("Heuss", "Germany", inplace = True)
BS_Df["Residence"].unique()


# In[11]:


BS_Df["Residence"].replace("Berlin", "Germany", inplace = True)
BS_Df["Residence"].unique()


# In[12]:


BS_Df["Residence"].replace("Deutschland", "Germany", inplace = True)
BS_Df["Residence"].replace('Germany ', "Germany", inplace = True)
BS_Df["Residence"].replace('Ireland ', "Ireland", inplace = True)
BS_Df["Residence"].replace('France ', "France", inplace = True)
BS_Df["Residence"].replace('United kingdom', "United Kingdom", inplace = True)
BS_Df["Residence"].replace('Uk', "United Kingdom", inplace = True)
BS_Df["Residence"].replace('Austria ', "Austria", inplace = True)
BS_Df["Residence"].replace('Switzerland / germany', "Switzerland & Germany", inplace = True)
BS_Df["Residence"].replace('Netherlands ', "Netherlands", inplace = True)
BS_Df["Residence"].replace('Czech republic ', "Czech Republic", inplace = True)
BS_Df["Residence"].replace('Belgium ', "Belgium", inplace = True)
BS_Df["Residence"].replace('Belgique', "Belgium", inplace = True)
BS_Df["Residence"].replace('Us', "USA", inplace = True)
BS_Df["Residence"].replace('Kildare', "Ireland", inplace = True)
BS_Df["Residence"].unique()


# In[13]:


BS_Df


# In[14]:


gender_counts = BS_Df["Gender"].value_counts()

plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Gender Representation')
plt.show()


# In[15]:


gender_counts


# In[16]:


age_counts = BS_Df["Age Group"].value_counts()

plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Age Group Representation')
plt.show()


# In[17]:


age_counts


# In[18]:


residence_counts = BS_Df["Residence"].value_counts()

plt.pie(residence_counts, labels=residence_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Residence Distribution')
plt.show()


# In[19]:


residence_counts


# In[20]:


MS_counts = BS_Df["Music Streaming Subscription"].value_counts()

plt.pie(MS_counts, labels=MS_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Music Streaming Subscription')
plt.show()


# In[21]:


MS_counts


# In[22]:


non_customers = BS_Df[["Gender", "Age Group", "Residence", "Music Streaming Subscription", "Reasons Non-Customers", "Music Listening by Non-Customers"]]
non_customers


# In[23]:


non_customers_df = non_customers[non_customers['Music Streaming Subscription'] == 'No']
non_customers_df


# In[24]:


non_customers_df["Reasons Non-Customers"].unique()


# In[25]:


non_customers_df["Reasons Non-Customers"].replace("Too prices", "Price (expensive)", inplace = True)
non_customers_df["Reasons Non-Customers"].replace('Too pricey', "Price (expensive)", inplace = True)
non_customers_df["Reasons Non-Customers"].replace("Too prices;I am not very interested in music", "Price & No Music Interest", inplace = True)
non_customers_df["Reasons Non-Customers"].replace("Too pricey;Freemium is sufficient for mee", "Price (expensive)", inplace = True)
non_customers_df["Reasons Non-Customers"].replace('Too pricey;I prefer physical ownership (CD, Vynil)', "Price & Physical Ownership", inplace = True)
non_customers_df["Reasons Non-Customers"].replace('I never really thought about it', "Not Considered Yet", inplace = True)
non_customers_df["Reasons Non-Customers"].replace("Heinz", "n/a", inplace = True)
non_customers_df["Reasons Non-Customers"].replace('Too pricey;I never really thought about it', "Price & Not Considered", inplace = True)
non_customers_df["Reasons Non-Customers"].replace('I prefer physical ownership (CD, Vynil)', "Physical Ownership", inplace = True)
non_customers_df["Reasons Non-Customers"].unique()


# In[26]:


non_customers_df


# In[27]:


non_customers_df["Music Listening by Non-Customers"].unique()


# In[28]:


non_customers_df["Music Listening by Non-Customers"].replace('Digital Downloads;Youtube;Free version of subscription services', "Digital Downloads & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Digital Downloads;Youtube;Spotify free', "Digital Downloads & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('I don´t listen to music', "No Music Listening", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;Youtube;Freemium Spotify', "Radio & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;Vynil records;Digital Downloads;Youtube', "Radio, Vynil & Digital Downloads", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;Digital Downloads', "Radio & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;Youtube;Concerts', "Radio, Concerts & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;Digital Downloads;Concerts', "Radio, Concerts & Freemium", inplace = True)
non_customers_df["Music Listening by Non-Customers"].replace('Radio;CDs;Youtube', "Radio, Vynil & Digital Downloads", inplace = True)
non_customers_df["Music Listening by Non-Customers"].unique()


# In[29]:


non_customers_df


# In[30]:


nc_gender_counts = non_customers_df["Gender"].value_counts()

plt.pie(nc_gender_counts, labels=nc_gender_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Non-Customer Gender Distribution')
plt.show()


# In[31]:


nc_gender_counts


# In[32]:


nc_age_counts = non_customers_df["Age Group"].value_counts()

plt.pie(nc_age_counts, labels=nc_age_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Non-Customer Age Group Distribution')
plt.show()


# In[33]:


nc_age_counts


# In[34]:


nc_residence_counts = non_customers_df["Residence"].value_counts()

plt.pie(nc_residence_counts, labels=nc_residence_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Non-Customer Residence Distribution')
plt.show()


# In[35]:


nc_residence_counts


# In[36]:


nc_reasons_counts = non_customers_df["Reasons Non-Customers"].value_counts()

plt.pie(nc_reasons_counts, labels=nc_reasons_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Non-Customer Reasons Distribution')
plt.show()


# In[37]:


nc_reasons_counts


# In[38]:


nc_ML_counts = non_customers_df["Music Listening by Non-Customers"].value_counts()

plt.pie(nc_ML_counts, labels=nc_ML_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Non-Customer Music Listening')
plt.show()


# In[39]:


nc_ML_counts


# In[40]:


customers_columns = ["Gender", 
                     "Age Group", 
                     "Residence", 
                     "Music Streaming Subscription", 
                     "Music Streaming Platform",
                     "Reasons for Platform", 
                     "Subscription Model", 
                     "Music Streaming Frequency",
                     "Music Streaming Devices",
                     "Music Streaming Occasions",
                     "Platform Satisfaction",
                     "Reasons for Satisfaction",
                     "Reasons for Dissatisfaction",
                     "Interface Appeal",
                     "High-quality Audio",
                     "Cross-Platform Syncing",
                     "Shared Playlists",
                     "Live Lyrics Integration",
                     "Smart Speaker Integration",
                     "Concert & Event Integration",
                     "Podcast",
                     "Offline Mode",
                     "Live Streaming Events",
                     "Sleep Timer",
                     "Genre-Based Radio Stations",
                     "Music Videos",
                     "Personalized Recommendations", 
                     "Vast Music Library", 
                     "Exact Search and Discovery",
                     "Enhances Artist Pages", 
                     "User Reviews and Ratings",
                     "Launch a Mix",
                     "Change Country Recommendations",
                     "Flow",
                     "Song Catcher",
                     "Music Quiz"]


# In[41]:


customers_df = BS_Df[customers_columns]
customers_df


# In[42]:


customers_df = customers_df[customers_df['Music Streaming Subscription'] == 'Yes']
customers_df


# In[43]:


customers_df['Music Streaming Subscription'].unique()


# In[44]:


customers_df['Music Streaming Platform'].unique()


# In[45]:


customers_df["Music Streaming Platform"].replace('SoundCloud (although i pay for spotify and not soundcloud)', "SoundCloud", inplace = True)
customers_df["Music Streaming Platform"].replace('Amazon prime', "Amazon Music", inplace = True)
customers_df['Music Streaming Platform'].unique()


# In[46]:


customers_df


# In[47]:


customers_df['Subscription Model'].unique()


# In[48]:


customers_df['Subscription Model'].replace('Somebody else’s hehe', "n/a", inplace = True)
customers_df['Subscription Model'].replace('Part of Amazon Prime', "Free", inplace = True)
customers_df['Subscription Model'].unique()


# In[49]:


customers_df


# In[50]:


customers_df["Reasons for Satisfaction"].unique()


# In[51]:


customers_df["Reasons for Dissatisfaction"].unique()


# In[52]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# In[53]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline


# In[54]:


#Satisfaction Analysis


# In[55]:


data = ["All Artists, good price", "all the music, + free podcasts and audiobooks", "Great price, good exclusives, every song is available", 
        "I am able to listen my most favorite music", "I could find all music i wann and i Love the albums", 
        "Does what I need it to do, since I rarely use it it doesn't bother me to much.",
        "it entertains me and has most artists, podcasts and music I want", 
        "I love the selection of music ", "Tbh I haven’t tried any of the others. Everything I want is on Spotify. I have all my playlists etc. I don’t want to change. ", 
        "Affordable student pricing, availability of songs and podcasts released exclusively to Spotify.", 
        "I don’t have to pay", "They offer everything I like to listen to and because it's affordable", 
        "i can listen to almost unlimited music ", "cheap, ease to use, nice interface, high quality audio", 
        "Offer, API; pricing, easy compatibility", "easy to use, broad variety of artists, podcasts", "All good", 
        "of the selection of music, device compatibility, podcasts and audio books available", 
        "All the music I need, recommendations to find new music I like, podcasts and audiobooks inclusive  ", 
        "I get great recommendations from the algorithm and discover new artists.",
        "it‘s easy to use and works very well with all my devices.", "I can listen to everything I want to listen to and download everything I want to",
        "Large selection of musics and easy of use ", "Lots of different music. ", "there is everything available I want to listen to ", 
        "I can find all the music I like ", "Audio quality is good", 
        "I can download music and listen to it while offline. I like that the playlists have the album covers on them. I like the que song feature a lot. I also like that you can go into settings and see a list of songs you have listened to. ",
        "I can easy find all the songs I want, custom playlists are pretty good", 
        "Spotify always recommends me the best music and it always fits to my taste ", 
        "I can find and listen to nearly everything", "You can listen to the music offline.", 
        "it has all the music I want, and my parents pay for it ", "Several features, easy to use ", 
        "Easy to use, well known platform", "Spotify is very practical", "They have all the music, its not limited ", 
        "It learns what you like and recommends new music", 
        "They have pretty much every song, easy to use, download and offline listening possible, suggestions for music similar to taste also good", 
        "The use of Apple Music is quite simple. Next to your own playlists that you create, there are multiple playlists already premade by Apple Music which I really enjoy if I’m getting tired of my own playlists. In addition Apple Music often gives recommandations of songs or artists which you could also enjoy and this allows you to discover new artists. ",
        "it’s so easy to use", "It's easy, with a lot of variety", "it works", 
        "it’s easy to use, works well on my Apple products, is cheap ", 
        "Songtexts, everything I need is there", 
        "variety of artists, features their live sets and remixes which spotify doesn’t have ", 
        "User experience is great, Spotify generally has all the songs/ artists I want to listen to, great podcast selection, Spotify wrap is fun", 
        "No publicity and easy to use ", "Ease of use, design, compatibility with other devices", 
        "I always find everything I’m looking for ", "They have all kind of music ", 
        "Excellent music selection", "It’s my music ", "It has all the titles I wanna hear.",
        "has everything i need music wise", "Of the selection", 
        "Spotify is easy to use, and I use it all the time",
        "Simple, effiecient usage, New music discovery simplified through music sharing communities, public playlists, I can see what my friends are listening to, … + Spotify Wrapped experience end of the year",
        "easy usage and new functions like session sharing",
        "I have been using Spotify premium for years now and have never had any problems.",
        "it is super easy to use", "Its free", "Convenient"]

df = pd.DataFrame(data, columns=["Reasons for Satisfaction"])


# In[56]:


vectorizer = TfidfVectorizer(stop_words='english')
kmeans = KMeans(n_clusters=5, random_state=42)
svd = TruncatedSVD(n_components=2)  

pipeline = make_pipeline(vectorizer, svd, kmeans)

df["Reasons for Satisfaction"].fillna("", inplace=True)

df['Satisfaction Cluster'] = pipeline.fit_predict(df["Reasons for Satisfaction"])

print(df[['Reasons for Satisfaction', 'Satisfaction Cluster']])


# In[57]:


df["Satisfaction Cluster"].unique()


# In[58]:


#Price-performance ratio
cluster_2_data = df[df["Satisfaction Cluster"] == 2]
cluster_2_data


# In[59]:


cluster2_lst = cluster_2_data["Reasons for Satisfaction"].unique()
cluster2_lst


# In[60]:


customers_df['Satisfaction Clusters'] = ""
customers_df


# In[61]:


customers_df.loc[customers_df['Reasons for Satisfaction'].isin(cluster2_lst), "Satisfaction Clusters"] = 2
customers_df


# In[62]:


#Content Variety and Availability
cluster_0_data = df[df['Satisfaction Cluster'] == 0]
cluster_0_data


# In[63]:


cluster0_lst = cluster_0_data["Reasons for Satisfaction"].unique()
cluster0_lst


# In[64]:


customers_df.loc[customers_df['Reasons for Satisfaction'].isin(cluster0_lst), "Satisfaction Clusters"] = 0
customers_df


# In[65]:


#User-Friendly Interface and Features
cluster_3_data = df[df['Satisfaction Cluster'] == 3]
cluster_3_data


# In[66]:


cluster3_lst = cluster_3_data["Reasons for Satisfaction"].unique()
cluster3_lst


# In[67]:


customers_df.loc[customers_df['Reasons for Satisfaction'].isin(cluster3_lst), "Satisfaction Clusters"] = 3
customers_df


# In[68]:


#Easy usage
cluster_1_data = df[df['Satisfaction Cluster'] == 1]
cluster_1_data


# In[69]:


cluster1_lst = cluster_1_data["Reasons for Satisfaction"].unique()
cluster1_lst


# In[70]:


customers_df.loc[customers_df['Reasons for Satisfaction'].isin(cluster1_lst), "Satisfaction Clusters"] = 1
customers_df


# In[71]:


#Access and Personalization
cluster_4_data = df[df['Satisfaction Cluster'] == 4]
cluster_4_data


# In[72]:


cluster4_lst = cluster_4_data["Reasons for Satisfaction"].unique()
cluster4_lst


# In[73]:


customers_df.loc[customers_df['Reasons for Satisfaction'].isin(cluster4_lst), "Satisfaction Clusters"] = 4
customers_df


# In[74]:


customers_df[['Reasons for Satisfaction', "Satisfaction Clusters"]]


# In[75]:


SC1_counts = customers_df["Satisfaction Clusters"].value_counts()
SC1_counts


# In[76]:


filtered_rows = customers_df[customers_df['Reasons for Satisfaction'].notnull() & (customers_df['Satisfaction Clusters'] == "")]
filtered_rows


# In[77]:


filtered_rows2 = customers_df[customers_df['Reasons for Satisfaction'].notnull() & (customers_df['Satisfaction Clusters']== 2)]
filtered_rows2


# In[78]:


filtered_rows = customers_df[(customers_df['Reasons for Satisfaction'] != "") & (customers_df['Satisfaction Clusters'] == "")]
filtered_rows


# In[79]:


filtered_rows[['Reasons for Satisfaction', "Satisfaction Clusters"]]


# In[80]:


customers_df.at[0, 'Satisfaction Clusters'] = 2
customers_df.at[2, 'Satisfaction Clusters'] = 0
customers_df.at[3, 'Satisfaction Clusters'] = 2
customers_df.at[6, 'Satisfaction Clusters'] = 0
customers_df.at[34, 'Satisfaction Clusters'] = 0
customers_df.at[38, 'Satisfaction Clusters'] = 4
customers_df


# In[81]:


SC_counts = df["Satisfaction Cluster"].value_counts()

plt.pie(SC_counts, labels=SC_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Satisfaction Reasons')
plt.show()


# In[82]:


SC_counts


# In[83]:


#Dissatisfaction Analysis


# In[84]:


data2 = ["No smooth way to the next song ", "nan", '-',
       'it is sometimes buggy',
       'I would like better tailored suggestions and I wish there were more stats available as with Spotify and the ability to compare/share playlists with friends ',
       'Notifications aren’t accurate and are hit or miss when wanting to be notified about new podcast releases.',
       'it is hard to find new music that is actually to my taste on the platform itself',
       'lots of good playlists are found on other platforms and can‘t be transferred, from time to time, songs are taken offline/disappear',
       'Lack of unlicensed music ', 'Price per Usage is to high ',
       'many suggested playlists are not relevant and I cannot stop the recommendations showing up, individual songs in blend cannot be deleted',
       'There could be better recommendations ',
       'SoundCloud features: amateurs and wider catalog', 'Expensive ',
       'It is relatively pricey ',
       'Streaming quality could be better, Apple Music for example has better quality ',
       'The song titles are not displayed in their native language ',
       'I would like them to improve the folders for playlists. It’s messy and hard to use. For non-students the price is high.  The new ai DJ feature on spotify is bad and keeps playing the same songs over and over again. ',
       'Certain songs are missing', '- ',
       'Spotify have unethical buisness practices and exploit small artists',
       'Spotify has better podcasts',
       'I can’t share or create playlists with Spotify users in group setting',
       'I have the feeling that sometimes not all songs can be streamed on Apple Music. Especially songs or albums from artists that aren’t maybe as famous yet. ',
       'i have to pay',
       'Spotify has a very small range of Classical Music',
       'It doesn’t have a good yearly wrap up system ',
       'Very few audiobooks',
       'there is ads but i am aware that this wouldn’t be an issue if i paid for it',
       'Sometimes the algorithm could be better at suggesting new songs that I could like',
       'Lack of playlist in comparison to e.g. Spotify ',
       'Occasional technical errors (playback not available until restart)',
       'Certain remixes or unreleased songs aren’t on Spotify',
       'Choice is bad', 'Very limited usability']

y_df = pd.DataFrame(data2, columns=["Reasons for Dissatisfaction"])


# In[85]:


vectorizer = TfidfVectorizer(stop_words='english')
kmeans = KMeans(n_clusters=5, random_state=42)
svd = TruncatedSVD(n_components=2)  

pipeline = make_pipeline(vectorizer, svd, kmeans)

y_df['Dissatisfaction Cluster'] = pipeline.fit_predict(y_df["Reasons for Dissatisfaction"])

print(y_df[['Reasons for Dissatisfaction', 'Dissatisfaction Cluster']])


# In[86]:


customers_df['Dissatisfaction Clusters'] = ""
customers_df


# In[87]:


#Price (expensive) and limited usability
cluster_0_dataY = y_df[y_df['Dissatisfaction Cluster'] == 0]
cluster_0_dataY


# In[88]:


cluster0_lstY = cluster_0_dataY["Reasons for Dissatisfaction"].unique()
cluster0_lstY


# In[89]:


customers_df.loc[customers_df['Reasons for Dissatisfaction'].isin(cluster0_lstY), 'Dissatisfaction Clusters'] = 0
customers_df


# In[90]:


#Limited Soundtracks and Genres
cluster_1_dataY = y_df[y_df['Dissatisfaction Cluster'] == 1]
cluster_1_dataY


# In[91]:


cluster1_lstY = cluster_1_dataY["Reasons for Dissatisfaction"].unique()
cluster1_lstY


# In[92]:


customers_df.loc[customers_df['Reasons for Dissatisfaction'].isin(cluster1_lstY), 'Dissatisfaction Clusters'] = 1
customers_df


# In[93]:


#Limited Exclusiveness and Features
cluster_2_dataY = y_df[y_df['Dissatisfaction Cluster'] == 2]
cluster_2_dataY


# In[94]:


cluster2_lstY = cluster_2_dataY["Reasons for Dissatisfaction"].unique()
cluster2_lstY


# In[95]:


customers_df.loc[customers_df['Reasons for Dissatisfaction'].isin(cluster2_lstY), 'Dissatisfaction Clusters'] = 2
customers_df


# In[96]:


#Lacking Audio and Recommendations Quality 
cluster_3_dataY = y_df[y_df['Dissatisfaction Cluster'] == 3]
cluster_3_dataY


# In[97]:


cluster3_lstY = cluster_3_dataY["Reasons for Dissatisfaction"].unique()
cluster3_lstY


# In[98]:


customers_df.loc[customers_df['Reasons for Dissatisfaction'].isin(cluster3_lstY), 'Dissatisfaction Clusters'] = 3
customers_df


# In[99]:


#Insufficient Personalization and Inaccurate Notifications
cluster_4_dataY = y_df[y_df['Dissatisfaction Cluster'] == 4]
cluster_4_dataY


# In[100]:


cluster4_lstY = cluster_4_dataY["Reasons for Dissatisfaction"].unique()
cluster4_lstY


# In[101]:


customers_df.loc[customers_df['Reasons for Dissatisfaction'].isin(cluster4_lstY), 'Dissatisfaction Clusters'] = 4
customers_df


# In[102]:


DSC_counts = y_df["Dissatisfaction Cluster"].value_counts()

plt.pie(DSC_counts, labels=DSC_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Dissatisfaction Reasons')
plt.show()


# In[103]:


DSC_counts


# In[104]:


PS_counts = customers_df["Platform Satisfaction"].value_counts()
PS_counts


# In[105]:


plt.scatter(customers_df["Music Streaming Platform"], customers_df["Platform Satisfaction"])
plt.title("Relation between Platform and Platform Satisfaction")
plt.xlabel("Music Streaming Platform")
plt.ylabel("Satisfaction")
plt.show()


# In[106]:


#SoundCloud is two-times in the x-axis
customers_df["Music Streaming Platform"].unique()


# In[107]:


customers_df["Music Streaming Platform"].replace('SoundCloud ', "SoundCloud", inplace = True)
customers_df["Music Streaming Platform"].unique()


# In[108]:


satisfaction_counts = customers_df.groupby(["Music Streaming Platform", "Platform Satisfaction"]).size().reset_index(name='Count')
satisfaction_counts


# In[109]:


import seaborn as sns


# In[110]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=satisfaction_counts,
    x="Music Streaming Platform",
    y="Platform Satisfaction",
    size="Count",
    hue="Count",  
    palette="viridis",
    sizes=(50, 500),  
    alpha=0.7)

plt.title("Relation between Platform and Platform Satisfaction")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Count")
plt.xlabel("Music Streaming Platform")
plt.ylabel("Satisfaction")
plt.show()


# In[111]:


sc_counts = customers_df.groupby(["Music Streaming Platform", "Satisfaction Clusters"]).size().reset_index(name='Count')
sc_counts


# In[112]:


sc_counts = sc_counts[sc_counts['Satisfaction Clusters'] != '']
sc_counts


# In[113]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=sc_counts,
    x="Music Streaming Platform",
    y=sc_counts["Satisfaction Clusters"].astype(int),
    size="Count",
    hue="Count",  
    palette="viridis",
    sizes=(50, 500),  
    alpha=0.7)

plt.title("Relation between Platform and Reasons for Satisfaction")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Count")
plt.xlabel("Music Streaming Platform")
plt.ylabel("Reasons for Satisfaction")
plt.yticks(range(sc_counts["Satisfaction Clusters"].astype(int).min(), sc_counts["Satisfaction Clusters"].astype(int).max() + 1))
plt.show()


# In[114]:


dsc_counts = customers_df.groupby(["Music Streaming Platform", "Dissatisfaction Clusters"]).size().reset_index(name='Count')
dsc_counts


# In[115]:


dsc_counts = dsc_counts[dsc_counts['Dissatisfaction Clusters'] != '']
dsc_counts


# In[116]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=dsc_counts,
    x="Music Streaming Platform",
    y=dsc_counts["Dissatisfaction Clusters"].astype(int),
    size="Count",
    hue="Count",  
    palette="viridis",
    sizes=(50, 500),  
    alpha=0.7)

plt.title("Relation between Platform and Reasons for Dissatisfaction")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title="Count")
plt.xlabel("Music Streaming Platform")
plt.ylabel("Reasons for Dissatisfaction")
plt.yticks(range(dsc_counts["Dissatisfaction Clusters"].astype(int).min(), dsc_counts["Dissatisfaction Clusters"].astype(int).max() + 1))
plt.show()


# In[117]:


c_gender_counts = customers_df["Gender"].value_counts()

plt.pie(c_gender_counts, labels=c_gender_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Customers Gender Distribution')
plt.show()


# In[118]:


c_gender_counts


# In[119]:


c_age_counts = customers_df["Age Group"].value_counts()

plt.pie(c_age_counts, labels=c_age_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Customers Age Group Distribution')
plt.show()


# In[120]:


c_age_counts


# In[121]:


c_residence_counts = customers_df["Residence"].value_counts()

plt.pie(c_residence_counts, labels=c_residence_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Customer Residence Distribution')
plt.show()


# In[122]:


c_residence_counts


# In[123]:


platforms_counts = customers_df["Music Streaming Platform"].value_counts()

plt.pie(platforms_counts, labels=platforms_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Platform Usage Distribution')
plt.show()


# In[124]:


platforms_counts


# In[125]:


SM_counts = customers_df["Subscription Model"].value_counts()

plt.pie(SM_counts, labels=SM_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Subscription Model Distribution')
plt.show()


# In[126]:


SM_counts


# In[127]:


frequency_counts = customers_df["Music Streaming Frequency"].value_counts()

plt.pie(frequency_counts, labels=frequency_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Frequency of Music Streaming Distribution')
plt.show()


# In[128]:


frequency_counts


# In[129]:


interface_counts = customers_df["Interface Appeal"].value_counts()

plt.pie(interface_counts, labels=interface_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Interface Appeal Distribution')
plt.show()


# In[130]:


interface_counts


# In[131]:


feature1_counts = customers_df["Personalized Recommendations"].value_counts()

plt.pie(feature1_counts, labels=feature1_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title('Personalized Recommendations')
plt.show()


# In[132]:


feature1_counts


# In[133]:


feature2_counts = customers_df["Vast Music Library"].value_counts()

plt.pie(feature2_counts, labels=feature2_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Vast Music Library")
plt.show()


# In[134]:


feature2_counts


# In[135]:


feature3_counts = customers_df["Exact Search and Discovery"].value_counts()

plt.pie(feature3_counts, labels=feature3_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Exact Search and Discovery")
plt.show()


# In[136]:


feature3_counts


# In[137]:


feature4_counts = customers_df["Enhances Artist Pages"].value_counts()

plt.pie(feature4_counts, labels=feature4_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Enhances Artist Pages")
plt.show()


# In[138]:


feature4_counts


# In[139]:


feature5_counts = customers_df["User Reviews and Ratings"].value_counts()

plt.pie(feature5_counts, labels=feature5_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("User Reviews and Ratings")
plt.show()


# In[140]:


feature5_counts


# In[141]:


feature6_counts = customers_df["Launch a Mix"].value_counts()

plt.pie(feature6_counts, labels=feature6_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Launch a Mix")
plt.show()


# In[142]:


feature6_counts


# In[143]:


feature7_counts = customers_df["Change Country Recommendations"].value_counts()

plt.pie(feature7_counts, labels=feature7_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Change Country Recommendations")
plt.show()


# In[144]:


feature7_counts


# In[145]:


feature8_counts = customers_df["Flow"].value_counts()

plt.pie(feature8_counts, labels=feature8_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Flow")
plt.show()


# In[146]:


feature8_counts


# In[147]:


feature9_counts = customers_df["Song Catcher"].value_counts()

plt.pie(feature9_counts, labels=feature9_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Song Catcher")
plt.show()


# In[148]:


feature9_counts


# In[149]:


feature10_counts = customers_df["Music Quiz"].value_counts()

plt.pie(feature10_counts, labels=feature10_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Music Quiz")
plt.show()


# In[150]:


feature10_counts


# In[151]:


feature11_counts = customers_df["High-quality Audio"].value_counts()

plt.pie(feature11_counts, labels=feature11_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("High-quality Audio")
plt.show()


# In[152]:


feature11_counts


# In[153]:


feature12_counts = customers_df["Cross-Platform Syncing"].value_counts()

plt.pie(feature12_counts, labels=feature12_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Cross-Platform Syncing")
plt.show()


# In[154]:


feature12_counts


# In[155]:


feature13_counts = customers_df["Shared Playlists"].value_counts()

plt.pie(feature13_counts, labels=feature13_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Shared Playlists")
plt.show()


# In[156]:


feature13_counts


# In[157]:


feature14_counts = customers_df["Live Lyrics Integration"].value_counts()

plt.pie(feature14_counts, labels=feature14_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Live Lyrics Integration")
plt.show()


# In[158]:


feature14_counts


# In[159]:


feature15_counts = customers_df["Smart Speaker Integration"].value_counts()

plt.pie(feature15_counts, labels=feature15_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Smart Speaker Integration")
plt.show()


# In[160]:


feature15_counts


# In[161]:


feature16_counts = customers_df["Concert & Event Integration"].value_counts()

plt.pie(feature16_counts, labels=feature16_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Concert & Event Integration")
plt.show()


# In[162]:


feature16_counts


# In[163]:


feature17_counts = customers_df["Podcast"].value_counts()

plt.pie(feature17_counts, labels=feature17_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Podcast")
plt.show()


# In[164]:


feature17_counts


# In[165]:


feature18_counts = customers_df["Offline Mode"].value_counts()

plt.pie(feature18_counts, labels=feature18_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Offline Mode")
plt.show()


# In[166]:


feature18_counts


# In[167]:


feature19_counts = customers_df["Live Streaming Events"].value_counts()

plt.pie(feature19_counts, labels=feature19_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Live Streaming Events")
plt.show()


# In[168]:


feature19_counts


# In[169]:


feature20_counts = customers_df["Sleep Timer"].value_counts()

plt.pie(feature20_counts, labels=feature20_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Sleep Timer")
plt.show()


# In[170]:


feature20_counts


# In[171]:


feature21_counts = customers_df["Genre-Based Radio Stations"].value_counts()

plt.pie(feature21_counts, labels=feature21_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Genre-Based Radio Stations")
plt.show()


# In[172]:


feature21_counts


# In[173]:


feature22_counts = customers_df["Music Videos"].value_counts()

plt.pie(feature22_counts, labels=feature22_counts.index, autopct='%1.1f%%', textprops={'fontsize':6})
plt.title("Music Videos")
plt.show()


# In[174]:


feature22_counts


# In[175]:


customers_df.to_csv("C:/CarolineZiegler/Studium_DCU/7. Semester/Business Strategy/Customers Output File", index = False)


# In[176]:


non_customers_df.to_csv("C:/CarolineZiegler/Studium_DCU/7. Semester/Business Strategy/Non-Customers Output File", index = False)

