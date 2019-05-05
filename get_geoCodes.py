#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:43:35 2019

@author: Tamara Williams

In order to make sure the tweets I am getting are coming from people at the
Disney properties, I want to geo-select the tweets, so I have to find the 
right Twitter IDs

"""
import tweepy

# Consume:
CONSUMER_KEY    = '[Your Key Here]'
CONSUMER_SECRET = '[Your Key Here]'

# Access:
ACCESS_TOKEN  = '[Your Key Here]'
ACCESS_SECRET = '[Your Key Here]'

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  RUN ONCE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Setup access API to get geo data
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    
    api = tweepy.API(auth)
    return api
 
# Create API object
api = connect_to_twitter_OAuth()  

# find the place ids
DLC_geo = api.geo_search(lat=33.81217, long=-117.9190, granularity='neighborhood')
DLC_id = DLC_geo[0].id
print('Disneyland id is: ',DLC_id)
DCA_geo = api.geo_search(lat=33.8061, long=-117.9209, granularity='neighborhood')
DCA_id = DCA_geo[0].id
print('California Adventure id is: ',DCA_id)
#------------------------------------
#Disneyland id is:  0c2e6999105f8070
#California Adventure id is:  0c2e6999105f8070
#------------------------------------

WDW_MK_geo = api.geo_search(lat=28.419799, long=-81.581195, granularity='neighborhood')
WDW_MK_id = WDW_MK_geo[0].id
Epcot_geo = api.geo_search(lat=28.375962, long=-81.552506, granularity='neighborhood')
Epcot_id = Epcot_geo[0].id
WDW_AK_geo = api.geo_search(lat= 28.357839, long=-81.590577, granularity='neighborhood')
WDW_AK_id = WDW_AK_geo[0].id
WDW_HS_geo = api.geo_search(lat=28.357529, long=-81.558271, granularity='neighborhood')
WDW_HS_id = WDW_HS_geo[0].id
WDW_DTD_geo = api.geo_search(lat=28.373212, long=-81.514903, granularity='neighborhood')
WDW_DTD_id = WDW_DTD_geo[0].id
print('WDW Magic Kingdom id is: ',WDW_MK_id)
print('WDW Epcot id is: ',Epcot_id)
print('WDW Animal Kingdom id is: ',WDW_AK_id)
print('WDW Hollywood Studios id is: ',WDW_HS_id)
print('WDW Downtown Disney id is: ',WDW_DTD_id)

#------------------------------------
#WDW Magic Kingdom id is:  01c6165c7783155f
#WDW Epcot id is:  01c6165c7783155f
#WDW Animal Kingdom id is:  01c6165c7783155f
#WDW Hollywood Studios id is:  01c6165c7783155f
#WDW Downtown Disney id is:  01c6165c7783155f
#------------------------------------
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DONE WITH GEO SETUP, COPY TO SCRAPER
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
