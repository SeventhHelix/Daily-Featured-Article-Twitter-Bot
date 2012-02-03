import urllib2
import sys
import re
import tweepy
import datetime

CONSUMER_KEY = 'xxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

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

    day = str(datetime.datetime.today().day)

    # Grabs the wikipedia main page and gets the line with the featured article
    # Probably not the best way to do this... but it works
    url = 'http://toolserver.org/~skagedal/feeds/fa.xml'
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    con = urllib2.urlopen(req)

    search = day + '.*\<\/title\>'
    shortLine = re.search(search, str(con.read()))


    info = shortLine.group()
    #print info

    articleName = info

    articleName = articleName.replace(day + ": ", "")
    articleName = articleName.replace("</title>", "")

    articleURL = "/wiki/" + articleName.replace(' ', '_')

# Prints the article info vars
def printArticleInfo():
    print articleName
    print articleURL


def tweepyAuthAndTweet():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    message = "Today's Featured Article: " + articleName + " [en.wikipedia.org" + articleURL + "]"
    api.update_status(message)

if __name__ == "__main__":
    main()
