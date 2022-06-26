import requests
from requests.structures import CaseInsensitiveDict
import json
from dotenv import load_dotenv
import os

load_dotenv()
def Authorization():
    auth = CaseInsensitiveDict()
    auth["Accept"] = "application/json"
    auth["Authorization"] = "Bearer " + os.getenv("BEARER_TOKEN")
    return auth

def User(username):
    url = os.getenv("TWITTER_API") + "by/username/" + username + "?user.fields=created_at"
    response = requests.get(url, headers=Authorization())
    return json.loads(response.text)

def CheckUserExist(user):
    return 'data' in User(username=user)

def Tweets(id):
    url = os.getenv("TWITTER_API") + id + "/tweets?tweet.fields=created_at"
    response = requests.get(url, headers=Authorization())
    return json.loads(response.text)