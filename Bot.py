import praw
from dotenv import load_dotenv
import os
import requests 
import urllib.parse

load_dotenv("py.env")



reddit_instance = praw.Reddit(
    client_id= os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    username = "Image_IdentifierBot",
    password = os.getenv("PASSWORD"),
    user_agent= os.getenv("USER_AGENT")
    )

# print(reddit_instance.user.me())

# subreddit = reddit_instance.subreddit("pics")

# for submission in subreddit.hot(limit=10):
#     print('Url:', submission.url)
def Get_Image(reddit_url_code:str):
    submission = reddit_instance.submission(reddit_url_code)
    response = requests.get(submission.url)
    with open(f'Animepics/{submission.author}image.jpg', 'wb') as f:
        f.write(response.content)

Get_Image("1e5indg")