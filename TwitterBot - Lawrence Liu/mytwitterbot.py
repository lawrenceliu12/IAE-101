# mytwitterbot.py
# IAE 101, Fall 2020
# Project 04 - Building a Twitterbot
# Name: Lawrence Liu      
# netid: lawliu
# Student ID: 113376858

import sys
import time
import simple_twit
import random

def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    # Do not remove or change this function call.
    # Pass the variable "api" holding this Tweepy API object as the first
    # argument to simple_twit functions.
    api = simple_twit.create_api()
    simple_twit.version()
    
    # Project 04 Exercises
    
    # Exercise 1 - Get and print 10 tweets from your home timeline
    #tweetList = simple_twit.get_home_timeline(api, 10)
    #for i in tweetList:
    #   print("Twitter ID: " + ((str)(i.id)))
    #    print("Tweeted by: " + i.author.screen_name)
    #    print("Full Text: " + i.full_text)
    #    print("Likes: " + (str)(i.favorite_count))
    #    print()
    
    # Exercise 2 - Get and print 10 tweets from another user's timeline
    #tweetList = simple_twit.get_user_timeline(api, "realDonaldTrump", 10)
    #for i in tweetList:
    #    print("Twitter ID: " + ((str)(i.id)))
    #    print("Tweeted by: " + i.author.screen_name)
    #    print("Full Text: " + i.full_text)
    #    print("Likes: " + (str)(i.favorite_count))
    #    print()
        
    # Exercise 3 - Post 1 tweet to your timeline.
    #tweet = simple_twit.send_tweet(api, "? _ ?")
    #print(type(tweet))
        
    # Exercise 4 - Post 1 media tweet to your timeline.
    #mediaTweet = simple_twit.send_media_tweet(api, "._.", "stare.jpg")
    #print(type(mediaTweet))
    
    # YOUR BOT CODE BEGINS HERE
    tempT = ""
    tempP = ""
    count = 0
    
    reminders = ["Did you forget your house keys?",
                 "Did you forget your mask?",
                 "Did you forget your car keys?",
                 "Did you forget to turn off the stove?",
                 "Did you forget to use hand sanitizer?",
                 "Did you forget to drink water?",
                 "Did you forget to wash your hands for 20+ seconds with soap?",
                 "Did you forget to eat today?",
                 "Did you eat the necessary amount of food for breakfast?",
                 "Did you eat the necessary amount of food for lunch?",
                 "Did you eat the necessary amount of food for dinner?",
                 "Did you forget to do the laundry?",
                 "Did you forget to clean your house?",
                 "Did you forget to clean your room?",
                 "Did you forget to do your necessary work for the week?",
                 "Did you forget to study for any classes?",
                 "Did you forget to keep track of your work in a calendar?",
                 "Did you forget to fold your clothes?",
                 "Did you forget to charge your phone?",
                 "Did you forget to charge your laptop?",
                 "Did you forget to take a break every so often?",
                 "Did you forget to brush your teeth?",
                 "Did you forget to wash your face?"]

    pictures = ["C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder.gif",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder1.png",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder2.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder3.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder4.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder5.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder6.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder7.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder8.png",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder9.jpg",
                "C:/Users/Lawrence Liu/Desktop/TwitterBot/reminder10.jpg"]
    
    while True:
        tweet = random.choice(reminders)
        mediaTweet = random.choice(pictures)

        if tweet != tempT and mediaTweet != tempP:
            twitterTweet = simple_twit.send_media_tweet(api, tweet, mediaTweet)
            tempT = tweet
            tempP = mediaTweet
            count += 1
            print("Tweet ran " + ((str)(count)) + " time(s).")
            time.sleep(43200) #12 hours

            
# end def main()

if __name__ == "__main__":
       main()
