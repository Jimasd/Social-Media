import requests
import urllib

def get_twitter_token():
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    OAUTH_TOKEN = ""
    OAUTH_TOKEN_SECRET = ""
    return CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

def get_fb_access_token():
    #https://developers.facebook.com/tools/debug/accesstoken
    return "EAASb5iwJNNABADBKdZAGnZCIkHyCQDYo8ZAyf3JapkpicfZCAytA1OA5JAA5YqVWyEAdLlki5irWQXWmPhaLFuKyXW7InIOHOZCxkUFWaVB0pwcYI99bISzM1gj9KR8iOQREXp63aJVXcKIo2NBzPOPa3URLnpsafcJHsMVZAmVsDrJnesXO3m"

def get_instagram_access():
    CLIENT_ID = "7c350df69b7f4ea19eea025e9322d1d4"
    CLIENT_SECRET = "607ce66121af4640b0c976dca13371b0"
    REDIRECT_URI = "http://localhost/"
    base_url = "https://www.instagram.com/oauth/authorize/"
    url = "{}?client_id={}&redirect_uri={}&response_type=code&scope=public_content".format(base_url, CLIENT_ID,
                                                                                           REDIRECT_URI)
    return CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, url

def get_linkedIn_token():
    APPLICATION_KEY = "77sz7xsyipwcbr"
    APPLICATION_SECRET = "Uu0GTUboTEBOVfP7"
    RETURN_URL = "http://localhost:8888"
    return APPLICATION_KEY, APPLICATION_SECRET, RETURN_URL


