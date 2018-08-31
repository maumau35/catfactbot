import praw
import pdb
import re
import os
import prawcore
import requests
from praw.models import Message



reddit=praw.Reddit(client_id='',
                   client_secret='',
                   username='',
                   password='',
                   user_agent='')



done=['redditusername']
weird=[]



subreddit = reddit.subreddit('all')
comments = subreddit.stream.comments()

for comment in comments:
    author=comment.author
    try:
        if re.search("!catfact", comment.body):
            if ('dead' not in comment.body and
                'dog' not in comment.body and
                'kitty' not in comment.body and
                'suicide' not in comment.body and
                'died' not in comment.body):
                if author.name not in done and author.name not in weird:
                    if comment.subreddit not in ["depression","suicidewatch","pcmasterrace"]:
                        comment.body=comment.body.split("\n")
                        print("replying to {0}'s (catfact) comment: {1}".format(author.name, comment.body))
                        s1 = (s1['fact'])
                        s1 = str(s1)
                        pinda = ("""Here is random catfact for you /u/{0}. {1}
___
^^Hello, ^^I'm ^^a ^^bot ^^and ^^this ^^action ^^was ^^performed ^^automatically ^^for ^^questions ^^pm ^^me.""".format(author.name, s1)) 
                        print (pinda)



                        n=1
                        if n==1:
                            weird.append(author.name)   
                            print (weird)
                            comment.reply(pinda)
















    except:
        pass




      
