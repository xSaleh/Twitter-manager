'''
Create by @0xhunter
'''

import tweepy
import json
import time
from datetime import datetime

### Authorization 
api_key = "JQxixeTdeuMnf8NF94Z9aQ4j1"
api_secret = "T6iaGsFeRBbQ1gcvQsWlWeeh9vykFYzFeeD49IXK1CASscxyxb"

choice = input("""
1 - Follow
2 - mention
3 - like
4 - Retweet
""")
if choice == "1":
    file_name = 'users.json'
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        auth = tweepy.OAuthHandler(api_key, api_secret)
        screen_id = input("screen_id: ")
        for i in data["my_data"]:
            key = i["key"]
            secret = i["secret"]
            auth.set_access_token(key, secret)
            api = tweepy.API(auth,wait_on_rate_limit=True)
            if api.create_friendship(user_id=screen_id) == False:
                print("already followed!")
            else:
                api.create_friendship(user_id=screen_id)
                print("Following ---> " + screen_id)
            
    
elif choice == "2":
    file_name = 'users.json'
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data["my_data"]:
            key = i["key"]
            secret = i["secret"]

            auth = tweepy.OAuthHandler(api_key, api_secret)
            auth.set_access_token(key, secret)
            api = tweepy.API(auth,wait_on_rate_limit=True)
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            tweet_id = input("tweet id from url: ") # 1553472617318940674

            api.update_status(status = 'This should be the best option ' + dt_string, in_reply_to_status_id = tweet_id , auto_populate_reply_metadata=True)
            print("Reply sending ---> " + tweet_id)
            time.sleep(6)

elif choice == "3":
    try:
        file_name = 'users.json'
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            auth = tweepy.OAuthHandler(api_key, api_secret)
            like_tweet_id = input("Enter like id from url: ") # 1553472617318940674

            for i in data["my_data"]:
                key = i["key"]
                secret = i["secret"]
                auth.set_access_token(key, secret)
                api = tweepy.API(auth,wait_on_rate_limit=True)
                status = api.get_status(like_tweet_id)
                favorited = status.favorited
                if favorited == True: 
                    print("The user has already liked the tweet.") 
                else:
                    api.create_favorite(like_tweet_id)
                    print("Liked ---> " + like_tweet_id)
                time.sleep(3)
    except Exception:
        pass
    print(api.create_favorite(like_tweet_id))

elif choice == "4":
    file_name = 'users.json'
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        auth = tweepy.OAuthHandler(api_key, api_secret)
        retweet_tweet_id = input("tweet id to retweet: ") # 1553472617318940674
        for i in data["my_data"]:
            key = i["key"]
            secret = i["secret"]
            auth.set_access_token(key, secret)
            api = tweepy.API(auth,wait_on_rate_limit=True)
            status = api.get_status(retweet_tweet_id)
            retweeted = status.retweeted 
            if retweeted == False:
                api.retweet(retweet_tweet_id)
                print("Retweet ---> " + retweet_tweet_id)
                time.sleep(6)
            else:
                print("already retweeted!")
else:
    print("Your choice is incorrect! ...exit")
    exit()
