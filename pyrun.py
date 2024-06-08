from requests_oauthlib import OAuth2Session
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
auth_url, state = session.authorization_url(auth_base_url)

print(f"\nClick here to authorize!! {auth_url}")
auth_response = input(f"\nPaste the full callback URL here: ") # From redirect url, only cope code portion

token_url = "https://www.strava.com/api/v3/oauth/token"
token = session.fetch_token(
    token_url,
    authorization_response=auth_response,
    include_client_id=True,
    client_id=client_id,
    client_secret=client_secret,
)

get_url = "https://www.strava.com/api/v3/athlete"
response = session.get(get_url)
print(f"\nResponse Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elapsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}")


