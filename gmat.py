import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import praw
import pandas as pd


reddit = praw.Reddit(client_id='****',
                     client_secret='****',
                     password='****',
                     user_agent='testscript by /u/licknux',
                     username='licknux')

posts = []
ml_subreddit = reddit.subreddit('gmat')
for post in ml_subreddit.hot(limit=450):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

print('posts').encode('utf-8')

posts.to_csv('gmat.csv', index=False)
