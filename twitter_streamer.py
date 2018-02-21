import tweepy, discord, asyncio

class MyStreamListener(tweepy.StreamListener):
    """Tweepy to stream Twitter feeds, stream starts when class is instanced."""

    def __init__(self, client, settings, token_instance, api=None):
        self.api = api or tweepy.API()
        self.client = client
        self.settings = settings
        self.token = token_instance
        self.start_stream()

    def on_status(self, status):
        """What to do when a new status is streamed in."""
        if not status.text.startswith('RT @WarframeAlerts'):
            if any(s in status.text for s in self.settings.twt_search_strings):
                print("\n--- Important Alert Detected! ---")
                sendmsg = asyncio.run_coroutine_threadsafe(
                    self.client.send_message(discord.Object(
                    id='395778918420054018'), status.text), self.client.loop)
                sendmsg.result(1200)
            print(status.text, '\n')

    def on_error(self, status_code):
        print('Error: ', status_code)
        return True # Maybe will prevent stream from dying?

    def on_timeout(self):
        print("Timeout...")
        return True # Maybe will prevent stream from dying?

    def start_stream(self):
        """Start Twitter stream."""
        self.auth = tweepy.OAuthHandler(self.token.twt_consumer_key,
                           self.token.twt_consumer_secret)
        self.auth.set_access_token(self.token.twt_access_token,
                              self.token.twt_access_secret)
        my_stream = tweepy.Stream(self.auth, self)
        try:
            my_stream.filter(follow=['1344755923'], async=True)
            # WarframeAlerts 1344755923
            # Isentil        579197344
        except (ReadTimeoutError, socket.timeout) as exc:
            print('\nTimeout caught, attempting to restart...')
            my_stream.filter(follow=['1344755923'], async=True)

