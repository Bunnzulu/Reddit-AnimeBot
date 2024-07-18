import praw
from dotenv import load_dotenv
import os
from Letters import CountLetters
load_dotenv("py.env")

reddit_instance = praw.Reddit(
    client_id= os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    username = os.getenv("UNAME"),
    password = os.getenv("PASSWORD"),
    user_agent= os.getenv("USER_AGENT")
)

subreddit = reddit_instance.subreddit('testingground4bots')

TRIGGER1 = "!SelfCommentCount"
TRIGGER2 = "!PostBodyCount"
TRIGGER3 = "!PostTitleCount"
TRIGGER4 = "!PostCount"
TRIGGER5 = "!ReplyCount"
TRIGGER6 = "!AllCommentCount"

for comment in subreddit.stream.comments(skip_existing=True):
    try:
        if TRIGGER1 in comment.body:
            script_output = CountLetters(comment.body)  
            comment.reply(f"This Comment's Stats:\n{script_output[0]}.\n{script_output[1]}")
        elif TRIGGER2 in comment.body:
            script_output = CountLetters(comment.submission.selftext)  
            comment.reply(f"This Post's Stats:\n{script_output[0]}.\n{script_output[1]}")
        elif TRIGGER3 in comment.body:
            script_output = CountLetters(comment.submission.title)  
            comment.reply(f"This Title's Stats:\n{script_output[0]}.\n{script_output[1]}")
        elif TRIGGER4 in comment.body:
            script_output = CountLetters(comment.submission.title+comment.submission.selftext)  
            comment.reply(f"This Post's combined Stats:\n{script_output[0]}.\n{script_output[1]}")
        elif TRIGGER5 in comment.body:
            parent = comment.parent()
            if type(parent) == praw.reddit.Comment:
                script_output = CountLetters(parent.body)  
                comment.reply(f"That Comment's Stats:\n{script_output[0]}.\n{script_output[1]}")
        elif TRIGGER6 in comment.body:
            List_of_Comments = []
            for c in comment.submission.comments.list():
                List_of_Comments.append(c.body)
            script_output = CountLetters("".join(List_of_Comments))  
            comment.reply(f"This Post's combined Stats:\n{script_output[0]}.\n{script_output[1]}")
    except:pass

