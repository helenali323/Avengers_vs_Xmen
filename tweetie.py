import sys
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def loadkeys(filename):
    """"
    load twitter api keys/tokens from CSV file with form
    consumer_key, consumer_secret, access_token, access_token_secret
    """
    with open(filename) as f:
        items = f.read().strip().split('\n')
        return items[1].split(',')


def authenticate(twitter_auth_filename):
    """
    Given a file name containing the Twitter keys and tokens,
    create and return a tweepy API object.
    """
    """""
    with open('twitter_auth_filename', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dict(row)

    consumer_key = dict(row)['consumer_key']
    consumer_secret = dict(row)['consumer_secret']
    access_token = dict(row)['access_token']
    access_token_secret = dict(row)['access_token_secret']
    """
    consumer_key, consumer_secret, access_token, access_token_secret= loadkeys(twitter_auth_filename)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def fetch_tweets(api, search_str):
    """
    Given a tweepy API object and the screen name of the Twitter user,
    create a list of tweets where each tweet is a dictionary with the
    following keys:

       id: tweet ID
       created: tweet creation date
       retweeted: number of retweets
       text: text of the tweet
       hashtags: list of hashtags mentioned in the tweet
       urls: list of URLs mentioned in the tweet
       mentions: list of screen names mentioned in the tweet
       score: the "compound" polarity score from vader's polarity_scores()

    Return a dictionary containing keys-value pairs:

       user: user's screen name
       count: number of tweets
       tweets: list of tweets, each tweet is a dictionary

    For efficiency, create a single Vader SentimentIntensityAnalyzer()
    per call to this function, not per tweet.
    """

    res = {}
    tweet_list = []
    analyser = SentimentIntensityAnalyzer()
    n = 0
    for status in tweepy.Cursor(api.search, q=search_str).items(200):
        n += 1
        dic = {}
        dic['id'] = status.id_str
        dic['created'] = status.user.created_at
        dic['retweeted'] = status.retweet_count
        dic['text'] = status.text
        dic['hashtags'] = status.entities.get('hashtags')
        text = status.text.replace('\n', ' ').split(' ')
        urls = [u for u in text if u.startswith('http')]
        if urls != []:
            dic['urls'] = urls[0]
        else:
            dic['urls'] = None
        mention = [v[1:-1] for v in text if v.startswith('@')]
        dic['mentions'] = mention
        dic['score'] = analyser.polarity_scores(status.text)['compound']
        tweet_list.append(dic)
        tweet_list = [i for n, i in enumerate(tweet_list) if i not in tweet_list[n + 1:]]
    res['count'] = n
    res['tweets'] = tweet_list
    return res



