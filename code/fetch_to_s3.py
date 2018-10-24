import requests
import requests.auth
import boto
import datetime
from boto.s3.key import Key
import json

#authenticate and get the access token
#get client id and secret by logging in to www.reddit.com/prefs/apps and create an app 
client_auth = requests.auth.HTTPBasicAuth('', '')
post_data = {"grant_type":"client_credentials"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
token=response.json()["access_token"]

#request programming trending posts
headers = {"Authorization": "bearer %s" % token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.get("https://oauth.reddit.com/r/programming/hot.json?limit=100", headers=headers)
filename = "reddit_%s.json" % datetime.datetime.today().strftime('%Y-%m-%d')
with open(filename, 'w') as outfile:
  json.dump(response.json()["data"]["children"], outfile)

#upload reddit json data to s3
conn = boto.connect_s3(host="s3.amazonaws.com")
bucket = conn.get_bucket("testing-datapipe")
k = Key(bucket)
k.key = "data/%s" % filename
k.set_contents_from_filename(filename)
