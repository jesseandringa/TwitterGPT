from requests_oauthlib import OAuth1Session
# import requests 
import os
import requests
import json
import openai 
import random

##GLOBAL 
insults = []
###insults to iterate through (randomly)
def getInsults():
    with open('resources/insults.txt','r') as file:
        for line in file:
            insults.append(line) 

### opens auth.json file to get required api key for http request
def getApiKey():
    with open('Auth/ChatGPTAuth.json', 'r') as file:
        json_data = json.load(file)
    return json_data["api_key"]
    # openai.organization = "1440"
    # openai.api_key = json_data["api_key"]
    # print(openai.Model.list())

### using prompt text, calls chat gpts api and returns the response text. 
def generateCompletion(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=100,  # Adjust the value based on the desired response length
        temperature=0.7,  # Controls the randomness of the output. Higher values (e.g., 0.8) make it more random, while lower values (e.g., 0.2) make it more deterministic.
        n=1,  # Specifies the number of completions to generate
        stop=None  # Set a string or list of strings to indicate when the response should stop
    )
    return response.choices[0].text.strip()

###cleans chatgpts completion of any chatgpt lingo
def cleanGPTResponse(completion):
    text = completion
    if completion.__contains__('ChatGPT: '):
        text = completion.replace('ChatGPT: ', "")
    if text.__contains__('Q: '):
        text = text.replace('Q: ', "")
        if text.__contains__('A: '):
            text = text.replace('A: ', "")
    elif text.__contains__('Setup: '):
        text = text.replace('Setup: ', "")
        if text.__contains__('Answer: '):
            text = text.replace('Answer: ', "")
    
    return text

### main method. given text prompt, it will format everything and then call the api
### returns the text completion. 
def getChatGPTResponse(prompt):
    
    openai.api_key = getApiKey()
    getInsults()
    randomIndex = random.randint(0, len(insults)-1)
    cuss = insults[randomIndex]
    format = "User: " #
    prompt = format +'Write a silly joke about the following summary'+  prompt + '.. make fun of the protagonist of the joke for being a '+cuss+'' +'''. Keep the joke to 240 characters maximum. Write the joke in the format style like \" Sea Turtle: humans keep trying to touch me while I\’m swimming.
    God: it could be worse.
    Sea Turtle: how?
    God: tell him crab.
    Crab: my legs are delicious.
    God: [nods] his legs are delicious. 
    
    or in the style of:
    [playing 7 minutes in heaven]
    
    doctor: ok lol plug him back in now'''
    
    completion = generateCompletion(prompt)
    text = cleanGPTResponse(completion)
    # print("ChatGPT: " + text)
    return text



    
# getChatGPTResponse("Russia's Wagner Group is really bad")


