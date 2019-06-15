from Secret import get_instagram_info, get_instagram_URL

import requests

CLIENT_ID, CLIENT_SECRET, REDIRECT_URI = get_instagram_info()
CODE = '' #get_instagram_URL()

payload = dict(client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                grant_type='authorization_code',
                redirect_uri=REDIRECT_URI,
                code=CODE)
response = requests.post('https://api.instagram.com/oauth/access_token', data = payload)
print(response.json())

ACCESS_TOKEN = response.json()['access_token']
print(ACCESS_TOKEN)