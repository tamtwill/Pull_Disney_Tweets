
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:43:35 2019

@author: Tamara Williams with help from Stackoverflow

I started with a script I found by searching on how to scrape Twitter.  I added
the geo-fencing and photo saving elements to it.

"""

import pandas as pd
import tweepy
import jsonpickle
import time
import csv
import wget


datapath = '~/Disney_Tweets/data/tmp/'
picpath = '~/Disney_Tweets/data/pics/'

dt = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())

# Consume:
CONSUMER_KEY    = '[Your key here]'
CONSUMER_SECRET = '[Your key here]'

# Access:
ACCESS_TOKEN  =  '[Your key here]'
ACCESS_SECRET =  '[Your key here]'


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
            
            #Convert to JSON format
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        #Display how many tweets we have collected
        print("Downloaded {0} tweets".format(tweetCount))
        
        piclist = list(tweets_with_media)
        
        print("list", piclist)
        filename = picpath+'tweetPics.csv'
        
        with open(filename,'w') as f:
            for item in piclist:
                f.write("%s\n" % item)
##            wr = csv.writer(resultFile)
##            wr.writerows(piclist)    
        for url in piclist:
            wget.download(url, out=picpath)

DLC_query = 'place:0c2e6999105f8070' \
    '#MagicKingdom OR #starwarsland OR #Disneyland OR #disneyland OR #DLC' \
    'OR #Batuu OR #DLR #starwars OR #disney OR #Disney OR  #disneylifestyle' \
    'OR #disneyphoto OR #disneypic  OR #disneyig OR #disneyfan OR #disneylandresort' \
    'OR #disneyblogger OR #disneyfun OR #annualpassholder OR #disneyvacation' \
    'OR #disneylove OR #disneygram OR #disneyaddict OR #disneyphotography ' \
    'OR #magickingdom OR #disneymagic OR #instadisney OR #happiestplaceonearth' \
    'OR #disneylover OR #disneyparks OR #pixar'

# Get those tweets
get_save_tweets('DLC_tweets.json', api, DLC_query, max_tweets = 250)
#get_save_tweets('DLC_tweets.json', api, DLC_query, max_tweets = 20)  ## for testing



WDW_query = 'place:01c6165c7783155f ' \
    '#MagicKingdom OR #starwarsland OR #Disneyworld OR #AnimalKingdom OR' \
    '#WDW OR #Hollywoodstudios OR #waltdisneyworld OR #epcot OR #DisneyWorld OR' \
    '#Disney OR #epcot OR #Epcot OR #AK OR #animalkingdom OR #typhoonlagoon' \
    'OR #MagicKingdom OR #starwarsland OR #Batuu OR #starwars OR ' \
    'OR #disney OR #Disney OR  #disneylifestyle' \
    'OR #disneyphoto OR #disneypic  OR #disneyig OR #disneyfan OR #disneylandresort' \
    'OR #disneyblogger OR #disneyfun OR #annualpassholder OR #disneyvacation' \
    'OR #disneylove OR #disneygram OR #disneyaddict OR #disneyphotography ' \
    'OR #magickingdom OR #disneymagic OR #instadisney OR #happiestplaceonearth' \
    'OR #disneylover OR #disneyparks OR #pixar'

# Get those tweets
get_save_tweets('WDW_tweets.json', api, WDW_query, max_tweets = 200)


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
        
tweets_df = tweets_to_df('DLC_tweets.json')
filename = datapath+'DLC_'+dt+'.csv'
tweets_df.to_csv(filename, sep=',', date_format = 'string', index = False, encoding = 'utf-8')

tweets_df = tweets_to_df('WDW_tweets.json')
filename = datapath+'WDW_'+dt+'.csv'
tweets_df.to_csv(filename, sep=',', date_format = 'string', index = False, encoding = 'utf-8')
