from requests_oauthlib import OAuth2Session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = "https://acontr9450.github.io/ac-stravaconnect/"
scope = ["profile:read_all"]

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url, 
                        scope=scope)

auth_base_url = "https://www.strava.com/oauth/authorize"
auth_link = session.authorization_url(auth_base_url)

print(f"Click here! {auth_link[0]}")
redirect_response = input(f"Paste code here: ")

token_url = "https://www.strava.com/api/v3/oauth/token"
payload = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': redirect_response,
    'grant_type': 'authorization_code'
}

response = requests.post(token_url, data=payload)
if response.status_code == 200:
    print("\n")
    print("Success!")
    print(response.json())  # Print the response in JSON format
else:
    print("\n")
    print("Error:", response.status_code)
    print(response.text)


