import util.NewsScraper as NS
import util.ChatGPTService as GPT
import util.TwitterService as TS

##GLOBALS##
newsURL = 'https://www.cnn.com/'
maxSummaryLength = 700
maxTweetLength = 280

def main ():
    #scrape news site for top article body
    url,headline = NS.getBreakingNewsArticle(newsURL)
    summary = NS.getArticleSummary(url)
    #keep string length short enough
    if(len(summary)>maxSummaryLength):
        summary = summary[:700]
    
    #create joke with article body using chatgpt
    joke = GPT.getChatGPTResponse(summary)
    
    print (joke)
    
    ##handle length issues since chatgpt is unpredictable
    if len(joke) > maxTweetLength: 
        print('joke is too long!!')
        joke1= joke[:maxTweetLength]
        joke2 = joke[maxTweetLength:]
        TS.postTweet(joke2)
        TS.postTweet(joke1)
    else:
        TS.postTweet(joke)
    
    

main()    

