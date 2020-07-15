import tweepy
import configparser
import json
import sys

config = configparser.ConfigParser()
config.read('config.ini')

# replace the following values with your Tweepy credentials.
consumer_key = config['Tweepy'][ 'CONSUMER_KEY']
consumer_secret = config['Tweepy'][ 'CONSUMER_SECRET']
access_token = config['Tweepy'][ 'ACCESS_TOKEN']
access_token_secret = config['Tweepy'][ 'ACCESS_TOKEN_SECRET']


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class Listener(tweepy.StreamListener):
    
    def __init__(self, output_file=sys.stdout):
        super(Listener,self).__init__()
        self.output_file = output_file
    
    def on_data(self, raw_data):
        data = json.loads(raw_data)
        print("@" + data["user"]["screen_name"])
        print(data["text"])
        print()
    
    def on_status(self, status):
        print("data received", file=self.output_file)
        print(status.text, file=self.output_file)
        print()
    
    def on_error(self, status_code):
        print(status_code, file=self.output_file)
        return False




#output = open('stream_output.txt', 'w', encoding="utf-8")
#listener = Listener(output_file=output)

listener = Listener()

stream = tweepy.Stream(auth=api.auth, listener=listener)

try:
    print('Start streaming.')
    stream.filter(track=['covid'])

except KeyboardInterrupt:
    print("Stopped.")

finally:
    print('Done.')
    stream.disconnect()
