# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:15:57 2016

Reddit Scraper

@author: Yuwen Wang
LJIWY
"""
import praw

# Info
APP_ID = "YfynvzstGodvnw"
APP_SECRET = "GZEEvlzl0dZorffUB_0aH0DmgDw"
USER_AGENT = "FineBros Buzz Tracker 1.0 by/u/xiaoyu7016"
URI = "http://www.example.com/unused/redirect/uri"


my_reddit = praw.Reddit(USER_AGENT)

QUERY = 'flair:react'
SUBREDDIT = 'videos'
PERIOD = 'month'

def fetch_submission_by_sort_criterion(query_string, subreddit_string, period_string, sort_criterion_string):
    """
    This function collect TOP 25 submissions
    from the specified query sorted by sorting criterion
    (1) query_string
        - how to build up query: https://www.reddit.com/wiki/search
    (2) subreddit_string: a string of subreddit name, e.g. 'videos'
    (3) period: time span
        - choices: 'day', 'month', 'year',' hour', etc.
    (4) sort_criterion_string:
        - choices: 'hot','new','comments', 'relevance', etc.
    - from a query(query_string) within a subreddit    
    """    
    submission_generator = my_reddit.search(query = query_string,
                                            subreddit = subreddit_string, 
                                            period = period_string,
                                            sort = sort_criterion_string) 
    submission_list = []    
    for thing in submission_generator:
        submission_list.append(thing)
    return submission_list
        

num_comments = fetch_submission_by_sort_criterion(QUERY,SUBREDDIT,PERIOD,'comments')
hot = fetch_submission_by_sort_criterion(QUERY,SUBREDDIT,PERIOD,'hot')
top = fetch_submission_by_sort_criterion(QUERY,SUBREDDIT,PERIOD,'top')
relevance = fetch_submission_by_sort_criterion(QUERY,SUBREDDIT,PERIOD,'relevance')

# Fetch the whole thread for the hottest submission
print hot[0].title
# Get all comments (this takes time)
hot[0].replace_more_comments(limit = None)

flatten_comments = praw.helpers.flatten_tree(hot[0].comments)

# Format and Output to csv
from pandas import Series, DataFrame
import pandas as pd

comment_list = []
for i in range(len(flatten_comments)):
    comment_i_dict = vars(flatten_comments[i])
    comment_i_Series = pd.Series(comment_i_dict.values(),
                                 index = comment_i_dict.keys())
    comment_list.append(comment_i_Series)
                        
hot_1_df = pd.concat(comment_list,axis=1)
hot_1_df = hot_1_df.transpose()

# This currently takes 5+ hours to write out 5K comments. 
# Need to 'shrink' the dataset before writing out
# Will first try to remove useless attributes
hot_1_df.to_csv('Hot1_Reddit Thread.csv',encoding = 'utf-8')

# Useful fields in object Submission
# title
# comments
# replace_more_comments

# Useful fields in object Comment
# is_root
# replies
# submission 

# Useful functions
# praw.helpers.flatten_tree



"""
BELOW ARE USELESS
"""

""" 
# Authorization -- turns out I don't need it at all =n=
my_reddit.set_oauth_app_info(client_id = APP_ID,
                             client_secret = APP_SECRET,
                             redirect_uri = URI)
url = my_reddit.get_authorize_url('uniqueKey',
                                  scope = 'identity',
                                  refreshable = False)
import webbrowser
webbrowser.open(url)
"""



"""
USERNAME = 
PASSWORD = 
APP_ID = "YfynvzstGodvnw"
APP_SECRET = "GZEEvlzl0dZorffUB_0aH0DmgDw"
USER_AGENT = "FineBros Buzz Tracker 1.0 by/u/xiaoyu7016"
URI = "http://www.example.com/unused/redirect/uri"

# Request token
REQUEST_URL = "https://www.reddit.com/api/v1/access_token"
client_auth = requests.auth.HTTPBasicAuth(APP_ID, APP_SECRET)
post_data = {
    "grant_type" : "password",
    "username" : USERNAME,
    "password" : PASSWORD
}
headers = {"User-Agent": USER_AGENT}

response = requests.post(REQUEST_URL, auth=client_auth, data=post_data, headers=headers)
response.json()

# Use token
USE_URL = "https://oauth.reddit.com/api/v1/me"
AUTH = str(response.json()['token_type']) + ' ' + str(response.json()['access_token'])
headers2 = {
    "Authorization" : AUTH,
    "User-Agent": USER_AGENT
}
response2 = requests.get(USE_URL, headers = headers2)
response2.json()





flair_react_url = "https://www.reddit.com/r/videos/search?q=flair%3Areact&restrict_sr=on"
react_content = my_reddit.get_content(flair_react_url)

react = []
for thing in react_content:
    react.append(thing)

ACCESS_INFO = my_reddit.get_access_information('JkjIWaOVVwAaFKdRtbbHz0PZtnc')
my_reddit.get_me()


USER_AGENT = "FineBros Buzz Tracker 1.0 by/u/xiaoyu7016"
r = praw.Reddit(user_agent = USER_AGENT)

user_name = "xiaoyu7016"
user = r.get_redditor(user_name)

gen = user.get_submitted()

karma_by_subreddit = {}

pprint.pprint(karma_by_subreddit)

subreddit = r.get_subreddit('video')

pprint(vars(subreddit))

url_video_react = "https://www.reddit.com/r/videos/search?q=flair%3Areact&restrict_sr=on"

video_sub = my_reddit.get_subreddit('videos')
comments_sample = video_sub.get_comments(limit = None)

comments=[]
for thing in comments_sample:
    comments.append(vars(thing))
    

for i in range(len(comments)):
    print comments[i]['author_flair_text']
