# Disney_Tweets
I wanted to collect some real-world data to use in personal programming projects.  Because I like Disney, and the new Star Wars areas will be opening at the US parks this summer, I decided to scrape tweets from Disney Parks as my data source.  It will be a while before the corpus is big enough to do much with, but in the meantime, data collection goes on.

The tweets are scraped via a cron job every 15 minutes.  At night, a second cron job opens the saved files, aggregates and de-dups the tweets.  The clean tweet collect is then written out for later analysis.

My goal is to look at several things
1) sentiment analysis, especially around the new area/attractions
2) general text analytics on the tweets
3) I am also grabbing tweet photos with the idea of using them as test data for a future image classification project
