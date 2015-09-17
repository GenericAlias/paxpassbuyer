# A bot that looks to buy friday and saturday passes to PAX Prime
# on the subreddit /r/paxpassexchange. If a submission
# matches the criteria searched for, the original poster
# of the submission will receive a PM as well as a comment
# on their submission telling them that they have been PM'd
import time
import praw
import random
from pprint import pprint
r = praw.Reddit('paxpassexchange monitor.')\
# Put your reddit user credentials here
r.login()
already_done = []
keywords = ['wts', 'prime']
types = ['fri', 'sat', 'full', 'fri-mon']
while True:
    subreddit = r.get_subreddit('paxpassexchange')
    for submission in subreddit.get_new(limit=2):
        op_title = submission.title.lower()
        author = submission.author
        is_wts = all(string in op_title for string in keywords)
        is_correct_days = any(string in op_title for string in types)
        if submission.id not in already_done and is_wts and is_correct_days:
            basemsg = " Shoot me a reply if you're still selling and I'll shoot you back payment info. Thanks!"
            if 'full' in op_title or 'fri-mon' in op_title:
                headmsg = ("Hey, I'm interested in buying pax passes. Ideally, I'd only want to buy 1 Friday and 1 Saturday pass, but if you're " +
                    "only willing to sell full sets I would also be interested in buying 1 full set as well. Either way, I'm interested!")
            elif "fri" in op_title and "sat" in op_title:
                headmsg = "Hey, I'm interested in buying 1 friday pass and 1 saturday pass."
            elif 'fri' in op_title:
                headmsg = "Hey, I'm interested in buying 1 friday pass."
            else:
                headmsg = "Hey, I'm interested in buying 1 saturday pass."
            msg = headmsg + basemsg
            r.send_message(author, "Buying Pax Passes", msg)
            submission.add_comment("Pm'd")
            print "New posting!: " + op_title
            already_done.append(submission.id)
            time.sleep(45 + random.randint(0, 30))
    time.sleep(5 + random.randint(0, 30))
