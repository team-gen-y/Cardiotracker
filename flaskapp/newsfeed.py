import feedparser

def parseRSS(rss_url):
    return feedparser.parse(rss_url)

def getHeadLines(rss_url):
    headlines = []

    feed = parseRSS(rss_url)
    for newitem in feed['items']:
        headlines.append(newitem)

    return headlines

allheadlines=[]

newsurls = {
    'health' : "https://www.mdlinx.com/xml/465.xml"
}

for key, url in newsurls.items():
    allheadlines.extend(getHeadLines(url))

def printout():
    for h in allheadlines:
        return h