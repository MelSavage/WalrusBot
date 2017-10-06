import discord
import asyncio

from bot_settings import Settings
from token_file import Token
from image_picker import ImagePicker
import message_functions as mf

settings = Settings()
token_instance = Token()
image_picker = ImagePicker()

client = discord.Client()

@client.event
async def on_ready():
    """Prints login confirmation in console"""
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')

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

client.run(token_instance.token)
