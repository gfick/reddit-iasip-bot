import praw

user_agent = ("IASIP Bot 0.1")

r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("iasip")
hot = subreddit.get_hot(limit =10)
hot_first = hot.next()
print hot_first.title