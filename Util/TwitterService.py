from requests_oauthlib import OAuth1Session
# import requests 
import os
import requests
import json


    
    # Convert the payload to a JSON string
def makePayLoad(text):
    json = {"text": text}
    # jsonPayload = json.dumps(json)
    return json



def  postTweet(text):
    payload = makePayLoad(text);
    
    #read auths from file     Auth/TwitterAuth.json
    with open('Auth/TwitterAuth.json', 'r') as file:
        json_data = json.load(file)

    # Access the data from the JSON object
    # For example, if the JSON structure is {"text": "Hello world!"}
    api_key = json_data["api_key"]
    api_key_secret = json_data["api_key_secret"]
    access_token = json_data["access_token"]
    access_token_secret = json_data["access_token_secret"]
    client_id = json_data["client_id"]
    client_secret = json_data["client_secret"]
    bearer_token = json_data["bearer_token"]
    
    
    consumer_key = api_key
    tweet_endpoint = 'https://api.twitter.com/2/tweets'
    
    # Print the extracted data
    print(api_key)
    # # Make the request
    # oauth = OAuth1Session(
    #     consumer_key = client_id,
    #     client_secret=client_secret,
    #     resource_owner_key=access_token,
    #     resource_owner_secret=access_token_secret,
        
    # )
    oauth = OAuth1Session(
        consumer_key,
        client_secret=api_key_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    # params = {
    #     'status': message
    # }

    response = oauth.post(tweet_endpoint, json=payload)

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True)) 
    
    
    
#script 
postTweet('Hi Tessssss')




