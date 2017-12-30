import discord, asyncio, logging, tweepy

from bot_settings import Settings
from token_file import Token
from image_picker import ImagePicker
import message_functions as mf

logging.basicConfig(level=logging.INFO)

settings = Settings()
token_instance = Token()
image_picker = ImagePicker()

client = discord.Client()

auth = tweepy.OAuthHandler(token_instance.twt_consumer_key,
                           token_instance.twt_consumer_secret)
auth.set_access_token(token_instance.twt_access_token,
                      token_instance.twt_access_secret)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        """What to do when a new status is streamed in."""
        if not status.text.startswith('RT @WarframeAlerts'):
            print(status.text)
            sendmsg = asyncio.run_coroutine_threadsafe(client.send_message(
                discord.Object(id='395778918420054018'), status.text),
                client.loop)
            # WarframeAlerts 395778918420054018
            # Isentil        579197344

    def on_error(self, status):
        print('Error: ', status)

@client.event
async def on_ready():
    """Prints login confirmation in console"""
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game_name = "- type {0}help to Taste the Walrus!"
    await client.change_presence(game=discord.Game(name=game_name.format(
        settings.prefix)))

@client.event
async def on_message(message):
    """Chat message triggers"""
    # %ping
    if message.content.startswith(settings.prefix + 'ping'):
        await mf.ping(client, message)
    # %mushroom
    elif message.content.startswith(settings.prefix + 'mushroom'):
        await mf.mushroom(client, message, image_picker)
    # %walrus        
    elif message.content.startswith(settings.prefix + 'walrus'):
        await mf.walrus(client, message, image_picker)
    # %angry8ball
    elif message.content.startswith(settings.prefix + 'angry8ball'):
        await mf.angry8ball(client, message)
    # %emote
    elif message.content.startswith(settings.prefix + 'emote'):
        await mf.emote(client, message)
    # %banana
    elif message.content.startswith(settings.prefix + 'banana'):
        await mf.banana(client, message, image_picker)
    # %aubergine
    elif message.content.startswith(settings.prefix + 'aubergine'):
        await mf.aubergine(client, message)
    # %help
    elif message.content.startswith(settings.prefix + 'help'):
        await mf.help(client, message, settings)

twitter_streamer = MyStreamListener()
my_stream = tweepy.Stream(auth, twitter_streamer)
my_stream.filter(follow=['1344755923'], async=True)

client.run(token_instance.token)
