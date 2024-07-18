import praw
from dotenv import load_dotenv
import os
from collections import Counter
load_dotenv("py.env")

Letters = "q,w,e,r,t,y,u,i,o,p,l,k,j,h,g,f,d,s,a,x,c,v,b,n,m"


reddit_instance = praw.Reddit(
    client_id= os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    username = os.getenv("UNAME"),
    password = os.getenv("PASSWORD"),
    user_agent= os.getenv("USER_AGENT")
    )



def CountLetters(text:str):
    n = 1
    Result = Counter(text)
    Most_used_letter = Result.most_common(n)
    while Most_used_letter[n-1][0] not in Letters.split(","):
        n += 1
        Most_used_letter = Result.most_common(n)
    Most_used_letters = f"The most used letter is {Most_used_letter[n-1][0]}. It appears {Most_used_letter[n-1][1]} times"
    All_Letters = f"The letters used are {list(filter(lambda x:x in Letters.split(","),set(Result.elements())))}."
    print(Most_used_letters)
    print(All_Letters)


subreddit = reddit_instance.subreddit("learnprogramming")

top_25_submissions = subreddit.new(limit=25)

for sub in top_25_submissions:
    print(sub.title)
    CountLetters(sub.selftext)
    print("--------------")


