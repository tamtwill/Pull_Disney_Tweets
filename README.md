# Disney_Tweets
I wanted to collect some real-world data to use in personal programming projects.  Because I like Disney, and the new Star Wars areas was opening at the US parks the summer I began this project, I decided to scrape tweets from Disney Parks as my data source.  The data were collected at a point in time before Elon Musk bought Twitter, and the data access policies changed.

The tweets are scraped via a cron job every 15 minutes.  At night, a second cron job opens the saved files, aggregates and de-dups the tweets.  The clean tweet collect is then written out for later analysis.

My goal is to look at several things
1) sentiment analysis, especially around the new area/attractions
2) general text analytics on the tweets
3) I am also grabbing tweet photos with the idea of using them as test data for a future image classification project.  Possibly training to recognize Mouse Ears, or the millenuim Falcon since the new "Land" has opened at DLR and will come online at WDW in August.
