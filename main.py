import util.NewsScraper as NS
import util.ChatGPTService as GPT
import util.TwitterService as TS

##GLOBALS##
newsURL = 'https://www.cnn.com/'

def main ():
    #scrape news site for top article body
    url,headline = NS.getBreakingNewsArticle(newsURL)
    summary = NS.getArticleSummary(url)
    
    #create joke with article body using chatgpt
    joke = GPT.getChatGPTResponse(summary)
    
    print (joke)
    
    TS.postTweet(joke)
    
    

main()    

