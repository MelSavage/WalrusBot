# WalrusBot
Discord bot based on Discord.py wrapper.

Uses Python 3.6, discord.py 0.16.12, and tweepy 3.5.0.

To use WalrusBot, install the Discord.py and Tweepy libraries. I am using the latest Tweepy from GitHub, rather than the one currently on PyPI, but both should work. However, the outdated version on PyPI currently has a bug that will interrupt the stream occasionally and require a program restart.


- To create the Token class necessary for logging in to Discord and Twitter's APIs:

1. create a file named token_file.py.

2. Structure the file like so:

class Token():
    def __init__(self):
        self.token = ''
        self.twt_consumer_key = ''
        self.twt_consumer_secret = ''
        self.twt_access_token = ''
        self.twt_access_secret = ''

3. self.token is for your Discord API key.

4. WalrusBot is set up to monitor a Twitter feed for Warframe alerts and message them to a channel. If you wish to monitor Twitter with your Discord bot, enter the twt_... API keys as well.


- The Twitter alerts are set up to go to a specific channel in our private Discord, you will need to change the UID of the messages' destination in twitter_streamer.py to your own channel. (Discord.object(id='xxx')) under the on_status method.
