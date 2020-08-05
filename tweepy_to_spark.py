# Required tweepy libraries.
import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

# Required supporting libraries (we will be sending json data through a socket).
import socket
import json

# Load your credentials from your config.ini file.
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Alternative to using a config.ini file: replace the following values with your credentials.
CONSUMER_KEY = config['Tweepy'][ 'CONSUMER_KEY']
CONSUMER_SECRET = config['Tweepy'][ 'CONSUMER_SECRET']
ACCESS_TOKEN = config['Tweepy'][ 'ACCESS_TOKEN']
ACCESS_SECRET = config['Tweepy'][ 'ACCESS_SECRET']

# Define TweetsListener, which inherits from the StreamListener class imported from tweepy.streaming.
# You can find Tweepy's source code for the StreamListener here: https://github.com/tweepy/tweepy/blob/v3.9.0/tweepy/streaming.py
class TweetsListener(StreamListener):

    # Constructor.
    def __init__(self, clientSocket):
        self.client_socket = clientSocket

    # Override on_data() function.
    def on_data(self, data):
        try:
            message = json.loads(data)                          # Load the json data.
            message_encoded = message['text'].encode('utf-8')   # Apply the correct character encoding.
            print(message_encoded)                              # For debugging.
            self.client_socket.send(message_encoded)            # Send the Tweepy data to our socket.
            return True
        except BaseException as ex:
            print("Error on_data: %s" % str(ex))
        return True

    def on_error(self, status):
        print(status)
        return True

def send_tweets(clientSocket):
    # Define your authentication.
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    Stream(auth, TweetsListener(clientSocket))                  # Follow the previously provided link for the Stream class' source code.

    # If you would like to filter the stream to focus it on a specific topic, (i.e.: 'covid'),
    # remove the previous line of code and uncomment the following:

    # twitter_stream = Stream(auth, TweetsListener(clientSocket))
    # twitter_stream.filter(track = ['covid'])                          




if __name__ == "__main__":
    print("Starting")

    new_socket = socket.socket()            # Initialize socket.
    TCP_IP = "127.0.0.1"                    # Socket IP (localhost).
    TCP_PORT = 9009                         # Socket port.

    new_socket.bind((TCP_IP, TCP_PORT))     # Bind the IP/Port.
    new_socket.listen(1)                    # Listen for a single connection.

    print("Socket created. Listening on port: %s" % str(TCP_PORT))

    client, address = new_socket.accept()   # Establish connection with client.
                                            # 'new_socket.accept()' returns a socket object (client),
                                            # and the address bound to said socket.

    print("Received request from: " + str(address))

    send_tweets(client)