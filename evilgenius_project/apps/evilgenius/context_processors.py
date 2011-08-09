from datetime import datetime

from django.conf import settings
from django.core.cache import cache

import twitter

def configuration(request):
    return {
        "settings": settings,
    }

def latest_tweets(request):
    tweets = cache.get("tweets")

    if tweets:
        return {"tweets": tweets}

    tweets = []

    for tweet in twitter.Api().GetUserTimeline(settings.TWITTER_USER)[:5]:
        tweet.date = datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y")
        tweets.append(tweet)

    cache.set("tweets", tweets, settings.TWITTER_TIMEOUT)
    
    return {"tweets": tweets}