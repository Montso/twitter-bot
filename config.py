import tweepy
import logging
import os

logger = logging.getLogger()


CONSUMER_KEY = "8wh03eNo85hokzGwUDHFoVF0P"
CONSUMER_SECRET = "XS2n9y2pJGsyj3NJZfMZsLH2KgAyH8Q7CFnU6aHdmNBaD4EzgK"
ACCESS_TOKEN = "1411985015005663237-g5Qys8uTNn7AfEv9QpnHwRu7TUp14I"
ACCESS_TOKEN_SECRET = "N5Y6cTpsgFrST0Y9ldtiivI8fo97gxQ7be6thVx3UGw7A"


def create_api():
    consumer_key = CONSUMER_KEY  #os.getenv("CONSUMER_KEY")
    consumer_secret = CONSUMER_SECRET #os.getenv("CONSUMER_SECRET")
    access_token = ACCESS_TOKEN #os.getenv("ACCESS_TOKEN")
    access_token_secret = ACCESS_TOKEN_SECRET #cos.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
        print("API created")
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api