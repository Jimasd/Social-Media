from Secret import get_reddit_peronal_account
import requests
from time import sleep

account = get_reddit_peronal_account()
account_comments = account + "comments/json"
sleep(2)
req = requests.get(account_comments)
print(req.text)