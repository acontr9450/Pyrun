from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_url = "https://acontr9450.github.io/ac-stravaconnect/"
scope = ["activity:read_all"]

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url, 
                        scope=scope)

auth_base_url = "https://www.strava.com/oauth/authorize"
auth_url, state = session.authorization_url(auth_base_url)

print(f"\nState: {state}")

print(f"\nClick here to authorize!! {auth_url}")
auth_response = input(f"\nPaste the full callback URL here: ")

token_url = "https://www.strava.com/api/v3/oauth/token"
token = session.fetch_token(
    token_url,
    authorization_response=auth_response,
    include_client_id=True,
    client_id=client_id,
    client_secret=client_secret,
)

get_url = "https://www.strava.com/api/v3/athlete/activities"
response = session.get(get_url)
print(f"\nResponse Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elapsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}")


# What info do i want?
# athleteid, name of activity, distance, moving_time, elapsed_time, total_elevation_gain, type, sport_type, workout_type
# id of activity, start_date, location_city, location_state, location_country, gear_id, average_cadence, average_heartrate,
# max_heartrate, elev_high, elev_low