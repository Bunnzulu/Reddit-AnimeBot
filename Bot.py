import praw
from dotenv import load_dotenv
import os
from Letters import CountLetters
load_dotenv("py.env")

# Reddit API credentials
reddit_instance = praw.Reddit(
    client_id= os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    username = os.getenv("UNAME"),
    password = os.getenv("PASSWORD"),
    user_agent= os.getenv("USER_AGENT")
)

# Define the subreddit to monitor
subreddit = reddit_instance.subreddit('testingground4bots')

# Define a command trigger
TRIGGER = "!testscript"

# Function to execute the script

# Monitor comments in the subreddit
for comment in subreddit.stream.comments(skip_existing=True):
    if TRIGGER in comment.body:
        # Run the Python script
        script_output = CountLetters(comment.body)
        
        # Reply to the comment with the script output
        comment.reply(f"This Comment's Stats:\n{script_output[0]}.\n{script_output[1]}")