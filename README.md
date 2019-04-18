# Avengers_vs_Xmen
Twitter sentiment analysis of two latest movies - Avengers: Endgame and X-men: Dark Phoenix

## Installation

I used Tweepy to scrape twitter data.

```sh
 pip install tweepy
```

In addition, In order to use tweepy, you may also need 
```sh
consumer_key = 'xxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

You can get them from the [Twitter Developer Platform](https://developer.twitter.com/)

## Usage example

I also produce a web server running at AWS to display the most recent 200 tweets from search result of endgame and dark phoenix. The web server respond with a tweet list color-coded by sentiment, using a red to green gradient: Red indicates negative while green represents positive. The example results (at 11pm 17th April 2019) are shown as below:

![Avengers]

![Xmen]

Obviously, X-men has more negative tweets (in red) than Avengers. The median sentiment scores also show the same result, with Avengers being positive and Xmen being negative. Thus, Avengers may claim victory in this round.



<!-- Markdown link & img dfn's -->
[Avengers]:https://github.com/helenali323/Avengers_vs_Xmen/blob/master/Avenger_result.png
[Xmen]:https://github.com/helenali323/Avengers_vs_Xmen/blob/master/Xmen_result.png
