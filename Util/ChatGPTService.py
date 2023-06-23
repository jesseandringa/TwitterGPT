from requests_oauthlib import OAuth1Session
# import requests 
import os
import requests
import json
import openai 

def getApiKey():
    with open('Auth/ChatGPTAuth.json', 'r') as file:
        json_data = json.load(file)
    return json_data["api_key"]
    # openai.organization = "1440"
    # openai.api_key = json_data["api_key"]
    # print(openai.Model.list())


def generate_completion(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=100,  # Adjust the value based on the desired response length
        temperature=0.7,  # Controls the randomness of the output. Higher values (e.g., 0.8) make it more random, while lower values (e.g., 0.2) make it more deterministic.
        n=1,  # Specifies the number of completions to generate
        stop=None  # Set a string or list of strings to indicate when the response should stop
    )
    return response.choices[0].text.strip()

def getChatGPTResponse(prompt):
    
    openai.api_key = getApiKey()

    format = "User: "
    prompt = format + "Say back to me: what's up bitch! but instead of saying \"bitch\" use the word swordfish"
    completion = generate_completion(prompt)
    print("ChatGPT: " + completion)
    return completion

getChatGPTResponse("hello")