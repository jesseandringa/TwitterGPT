import requests
from bs4 import BeautifulSoup
import json

#scrapes fox news' site for top article summary
def scrapeFox(soup):
    # mainDiv = soup.find('div', class_ = 'info ' )
    h3 = soup.find('h3',class_='title')
    print(h3)
    articleUrl = h3.find('a')
    articleUrl = articleUrl['href']
    # articleUrl = 1
    # print(articleUrl)
    return articleUrl,'titleFake'
  
#scrapes cnns site for top article summary  
def scrapeCnn(soup):
    # Find the main breaking news article
    articleUrl = soup.find('a', class_='container__title-url container_lead-package__title-url')
    # print('url tag: ')
    # print(articleUrl)
    url = articleUrl['href']
    # print('url: ' + url)
    articleHeadline = soup.find('h2', class_ = 'container__title_url-text container_lead-package__title_url-text')

    # Extract the headline text
    headline = articleHeadline.text.strip()
    return url,headline

# Send an HTTP GET request to CNN.com to get main breaking article
def getBreakingNewsArticle(url):
    # url = 'https://www.cnn.com/'
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)
    if 'www.foxnews.com' in url : 
        url, headline = scrapeFox(soup)
    elif 'www.cnn.com' in url :
        url, headline = scrapeCnn(soup)
        
    return url,headline


##reads list of urls. Checks to see if new url is in list. 
##returns true if in list already
##returns false if new. Then adds to list as well.
def timesUsed(url,numOfBodies):
    filePath = 'resources/articleUrls.json'
    with open(filePath, 'r') as file:
        urlData = json.load(file)
        #if url exists return value associated with it and incremenet value 
        if url in urlData:
            value = int(urlData.get(url))
            if value + 1 > numOfBodies:
                value = -1
            urlData[url] = value + 1
            with open(filePath, 'w') as fileWrite:
                json.dump(urlData,fileWrite,indent=4)
            return value
        #if not found. add it to the json obj
    urlData[url] = 0
    with open(filePath, 'w') as fileWrite:
        json.dump(urlData,fileWrite,indent=4)
    return 0


##gets article body/summary by using actual url then parsing.
def getArticleSummary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    # Find the script tag containing the JSON data
    try:
        scriptTag = soup.find('script', id='liveBlog-schema')
            # Extract the JSON data from the script tag
        jsonData = json.loads(scriptTag.string)
    # print(scriptTag)
    except: 
        scriptTag = soup.find('script',type="application/ld+json")
        jsonData = json.loads(scriptTag.string)

    # print(jsonData)

    # Extract the article body text
    
    try: 
        articleSummary = jsonData['liveBlogUpdate']
        article_bodies = [item['articleBody'] for item in articleSummary]
    except: 
        return jsonData['articleBody']

    # Print the first article bodies
    # print(article_bodies[0])
    articleNum = timesUsed(url,len(article_bodies))
    
    return article_bodies[articleNum]
    
    
#script
# url = 'https://www.cnn.com/'
# articleUrl,headline = getBreakingNewsArticle(url)
# getArticleSummary(articleUrl)

# a,b = getBreakingNewsArticle('https://www.foxnews.com/')
