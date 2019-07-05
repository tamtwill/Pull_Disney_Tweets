#!/usr/bin/env python3
##https://medium.com/@wilamelima/mining-twitter-for-sentiment-analysis-using-python-a74679b85546

import pandas as pd
import tweepy
import jsonpickle
import time
import csv
import wget
import os





datapath = [insert path]
picpath = [insert path]

dt = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

# Consume:
CONSUMER_KEY    = [insert your key]
CONSUMER_SECRET = [insert your key]

# Access:
ACCESS_TOKEN  = [insert your key]
ACCESS_SECRET = [insert your key]


##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##  RUN ONCE
##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
## Setup access API to get geo data
#def connect_to_twitter_OAuth():
#    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
#    
#    api = tweepy.API(auth)
#    return api
# 
## Create API object
#api = connect_to_twitter_OAuth()  
#
## find the place ids
#DLR_geo = api.geo_search(lat=33.81217, long=-117.9190, granularity='neighborhood')
#DLR_id = DLR_geo[0].id
#print('Disneyland id is: ',DLR_id)
#DCA_geo = api.geo_search(lat=33.8061, long=-117.9209, granularity='neighborhood')
#DCA_id = DCA_geo[0].id
#print('California Adventure id is: ',DCA_id)
##------------------------------------
##Disneyland id is:  0c2e6999105f8070
##California Adventure id is:  0c2e6999105f8070
##------------------------------------
#
#WDW_MK_geo = api.geo_search(lat=28.419799, long=-81.581195, granularity='neighborhood')
#WDW_MK_id = WDW_MK_geo[0].id
#Epcot_geo = api.geo_search(lat=28.375962, long=-81.552506, granularity='neighborhood')
#Epcot_id = Epcot_geo[0].id
#WDW_AK_geo = api.geo_search(lat= 28.357839, long=-81.590577, granularity='neighborhood')
#WDW_AK_id = WDW_AK_geo[0].id
#WDW_HS_geo = api.geo_search(lat=28.357529, long=-81.558271, granularity='neighborhood')
#WDW_HS_id = WDW_HS_geo[0].id
#WDW_DTD_geo = api.geo_search(lat=28.373212, long=-81.514903, granularity='neighborhood')
#WDW_DTD_id = WDW_DTD_geo[0].id
#print('WDW Magic Kingdom id is: ',WDW_MK_id)
#print('WDW Epcot id is: ',Epcot_id)
#print('WDW Animal Kingdom id is: ',WDW_AK_id)
#print('WDW Hollywood Studios id is: ',WDW_HS_id)
#print('WDW Downtown Disney id is: ',WDW_DTD_id)
#------------------------------------
#WDW Magic Kingdom id is:  01c6165c7783155f
#WDW Epcot id is:  01c6165c7783155f
#WDW Animal Kingdom id is:  01c6165c7783155f
#WDW Hollywood Studios id is:  01c6165c7783155f
#WDW Downtown Disney id is:  01c6165c7783155f
#------------------------------------
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DONE WITH GEO SETUP
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Setup access API
def connect_to_twitter_OAuth():
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    
    api = tweepy.API(auth)
    return api
 
# Create API object
api = connect_to_twitter_OAuth()  

def get_save_tweets(filepath, api, query, max_tweets, lang='en'):

    tweetCount = 0
    tweets_with_media = set()

    #Open file and save tweets
    with open(filepath, 'w') as f:

        # Send the query
        for tweet in tweepy.Cursor(api.search,q=query,lang=lang).items(max_tweets):  
#            print(tweet)
            
            media = tweet.entities.get('media',[])
            if (len(media)>0):
                tweets_with_media.add(media[0]['media_url'])
#            print(tweets_with_media)
                ## Handle screening out video
            
            #Convert to JSON format
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        #Display how many tweets we have collected
        print("Downloaded {0} tweets".format(tweetCount))
        
        piclist = list(tweets_with_media)
        
        print("list", piclist)
        if query == 'place:0c2e6999105f8070':
            park = 'DLR'
        if query == 'place:01c6165c7783155f' :
            park = 'WDW'
        
        filename = picpath+park+'/'+'tweetPics.csv'
        with open(filename,'w') as f:
            for item in piclist:
                f.write("%s\n" % item)
        
#        with open(filename,'w') as f:
#            for item in piclist:
#                f.write("%s\n" % item)
###            wr = csv.writer(f)
###            wr.writerows(piclist)    
#        for url in piclist:
#            wget.download(url, out=picpath)

#DLR_query = 'place:0c2e6999105f8070' \
#     '#MagicKingdom OR #starwarsland OR #Disneyland OR #disneyland OR #DLR' \
#     'OR #Batuu OR #DLR #starwars OR #disney OR #Disney'

DLR_query = 'place:0c2e6999105f8070' \
#    '#MagicKingdom OR #starwarsland OR #Disneyland OR #disneyland OR #DLC' \
#    'OR #Starwarsland OR #StarwarsLand OR #Starwars' \
#    'OR #Batuu OR #DLR OR #starwars OR #disney OR #Disney' \
#    'OR #disneyphoto OR #disneypic  OR #disneyig OR #disneyfan OR #disneylandresort' \
#    'OR #disneyblogger OR #disneyfun OR #disneyvacation' \
#    'OR #disneygram OR #disneyaddict OR #magickingdom OR #disneymagic' \
#    'OR #instadisney OR #happiestplaceonearth' \
#    'OR #disneyparks OR #pixar OR #Pixar OR #pixarpier'  
    
    
##  #disneylifestyle #californiadreaming #disneyphoto #disneypic #disneyig 
## #anaheim #picoftheday #disneyfan #disneylandresort #california #disneyblogger 
## #disneyfun #inspiration #annualpassholder #disneyvacation #disneylove #disneygram 
## #disneyaddict #disneyphotography #magickingdom #disneymagic #instadisney #adventure
## #happiestplaceonearth #disneylover #disneyparks #pixar

# Get those tweets
get_save_tweets('DLR_tweets.json', api, DLR_query, max_tweets = 225)
#get_save_tweets('DLR_tweets.json', api, DLR_query, max_tweets = 20)



#WDW_query = 'place:01c6165c7783155f ' \
#     '#MagicKingdom OR #starwarsland OR #Disneyworld OR #AnimalKingdom OR' \
#     '#WDW OR #Hollywoodstudios OR #waltdisneyworld OR #epcot OR #DisneyWorld OR' \
#     '#Disney'

WDW_query = 'place:01c6165c7783155f' \
#    '#MagicKingdom OR #starwarsland OR #Disneyworld OR #AnimalKingdom' \
#    'OR #WDW OR #waltdisneyworld OR #epcot OR #DisneyWorld' \
#    'OR #disneyworld OR #AK OR #animalkingdom '\
#    'OR #magickingdom OR #Magickingdom OR #Starwarsland OR #Batuu OR #starwars' \
#    'OR #disney OR #disneylifestyle OR #disneyphoto OR #disneypic  OR #disneyig OR #disneyfan' \
#    'OR #disneyfun OR #disneyvacation OR #disneygram OR #disneyphotography ' \
#    'OR #disneymagic OR #instadisney OR #happiestplaceonearth OR #disneyparks'

# Get those tweets
get_save_tweets('WDW_tweets.json', api, WDW_query, max_tweets = 225)


def tweets_to_df(path):
    
#    tweets = list(open('tweets_bkp.json', 'rt'))
#    tweets = list(open('tweets.json', 'rt'))
    tweets = list(open(path, 'rt'))
    
    text = []
    weekday = []
    month = []
    day = []
    hour = []
    hashtag = []
    url = []
    favorite = []
    reply = []
    retweet = []
    follower = []
    following = []
    user = []
    screen_name = []

    for t in tweets:
        t = jsonpickle.decode(t)
        
        # Text
        text.append(t['text'])
        
        # Decompose date
        date = t['created_at']
        weekday.append(date.split(' ')[0])
        month.append(date.split(' ')[1])
        day.append(date.split(' ')[2])
        
        time = date.split(' ')[3].split(':')
        hour.append(time[0]) 
        
        # Has hashtag
        if len(t['entities']['hashtags']) == 0:
            hashtag.append(0)
        else:
            hashtag.append(t['entities']['hashtags'])
            
        # Has url
        if len(t['entities']['urls']) == 0:
            url.append(0)
        else:
            url.append(1)
            
        # Number of favs
        favorite.append(t['favorite_count'])
        
        # Is reply?
        if t['in_reply_to_status_id'] == None:
            reply.append(0)
        else:
            reply.append(1)       
        
        # Retweets count
        retweet.append(t['retweet_count'])
        
        # Followers number
        follower.append(t['user']['followers_count'])
        
        # Following number
        following.append(t['user']['friends_count'])
        
        # Add user
        user.append(t['user']['name'])

        # Add screen name
        screen_name.append(t['user']['screen_name'])
        

        
    d = {'text': text,
         'weekday': weekday,
         'month' : month,
         'day': day,
         'hour' : hour,
         'has_hashtag': hashtag,
         'has_url': url,
         'fav_count': favorite,
         'is_reply': reply,
         'retweet_count': retweet,
         'followers': follower,
         'following' : following,
         'user': user,
         'screen_name' : screen_name
        }
    
    
    return pd.DataFrame(data = d)
        
tweets_df = tweets_to_df('DLR_tweets.json')
filename = datapath+'DLR/'+'DLR_all_'+dt+'.csv'
tweets_df.to_csv(filename, sep=',', date_format = 'string', index = False, encoding = 'utf-8')

tweets_df = tweets_to_df('WDW_tweets.json')
filename = datapath+'WDW/'+'WDW_all_'+dt+'.csv'
tweets_df.to_csv(filename, sep=',', date_format = 'string', index = False, encoding = 'utf-8')
