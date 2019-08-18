__author__ = 'david_000'
import feedparser
import requests

def getWeather():
    weatherData = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20%20*%20from%20weather.forecast%20where%20woeid=12778800&format=json')
    weatherData = weatherData.json()
    data = weatherData["query"]["results"]["channel"]["item"]
    try:
        val = data["title"], data["description"].replace('<![CDATA[', '').replace("Low", " Low")
        last_forecast_index = val[1].rfind(". ")
        val = val[0], val[1][:last_forecast_index+val[1][last_forecast_index:].find("\n")]

    except:
        val = "Unavailable", "Unavailable"
        
    return val

def getSports():
    tigersData = feedparser.parse('https://sports.yahoo.com/mlb/teams/det/rss.xml')
    redWingsData = feedparser.parse('https://sports.yahoo.com/nhl/teams/det/rss.xml')
    lionsData = feedparser.parse('https://sports.yahoo.com/nfl/teams/det/rss.xml')
    pistonsData = feedparser.parse('https://sports.yahoo.com/nba/teams/det/rss.xml')
    try:
        val1 = tigersData.entries[0].link, tigersData.entries[0].title
    except:
        val1 = "Unavailable", "Unavailable"
    try:
        val2 = redWingsData.entries[0].link, redWingsData.entries[0].title
    except:
        val2 = "Unavailable", "Unavailable"
    try:
        val3 = lionsData.entries[0].link, lionsData.entries[0].title
    except:
        val3 = "Unavailable", "Unavailable"
    try:
        val4 = tigersData.entries[0].link, tigersData.entries[0].title
    except:
        val4 = "Unavailable", "Unavailable"
        
    return val1[0], val1[1], val2[0], val2[1], val3[0], val3[1], val4[0], val4[1]

def getNews():
    newsData = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')
    try:
        val = newsData.entries[0].link, newsData.entries[0].title, newsData.entries[0].description, \
            newsData.entries[1].link, newsData.entries[1].title, newsData.entries[1].description, \
            newsData.entries[2].link, newsData.entries[2].title, newsData.entries[2].description, \
            newsData.entries[3].link, newsData.entries[3].title, newsData.entries[3].description, \
            newsData.entries[4].link, newsData.entries[4].title, newsData.entries[4].description
    except:
        val = ["Unavailable"]*15
        
    return val

def getHistory():
    historyData = feedparser.parse('http://www.history.com/this-day-in-history/rss')
    try:
        val = historyData.feed.link, historyData.entries[0].title
    except:
        val = "Unavailable", "Unavailable"
        
    return val
