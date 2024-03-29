import urllib2
import sys
import re
import tweepy
import datetime
import time

CONSUMER_KEY = '-----------------'
CONSUMER_SECRET = '--------------------------------------------'
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

articleName = ''
articleURL = ''

def main():
    getFeaturedArticleNameAndLink()
    #printArticleInfo()
    tweepyAuthAndTweet()


# Sets the articleName and articleURL
def getFeaturedArticleNameAndLink():
    global articleName
    global articleURL

    global day 
    day = str(datetime.datetime.today().day)

    global month
    month = datetime.datetime.now().strftime("%b");

    # Get an rss feed from instapaper of the featured articles
    url = 'http://www.instapaper.com/special/wikipedia_featured_rss'
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)

    # use regexp to parse the document and find today's article
    search = 'page\.\<\/description\>\<item\>\<title\>.*?\<\/title\>'
    shortLine = re.search(search, str(con.read()))


    info = shortLine.group()
    #print info

    articleName = info

    # Format the information
    articleName = articleName.replace("page.</description><item><title>", "")
    articleName = articleName.replace("</title>", "")

    articleURL = "/wiki/" + articleName.replace(' ', '_')

# Prints the article info vars
def printArticleInfo():
    print articleName
    print articleURL


# Authenticates and tweets the article
def tweepyAuthAndTweet():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    message = month + " " + day + ": " + articleName + " [en.wikipedia.org" + articleURL + "]"
    api.update_status(message)

if __name__ == "__main__":
    main()
