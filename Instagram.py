from Secret import get_instagram_access
import requests
import pandas as pd

CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, URL = get_instagram_access()

CODE = input("Manually input the code after '?code=...' in\n{}\nHere: ".format(URL))
payload = dict(client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                grant_type='authorization_code',
                redirect_uri=REDIRECT_URI,
                code=CODE)

response = requests.post('https://api.instagram.com/oauth/access_token', data=payload)
ACCESS_TOKEN = response.json()['access_token']

print(pd.DataFrame(response.json())["user"])
print(ACCESS_TOKEN)
print(CODE)