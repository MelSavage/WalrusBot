import discord
import asyncio

from bot_settings import Settings
from token_file import Token
# message_functions will store responses to chat message triggers.
import message_functions as mf

settings = Settings()
token_instance = Token()

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
    if message.content.startswith(settings.prefix + 'ping'):
        await mf.ping(client, message)

    elif message.content.startswith(settings.prefix + 'mushroom'):
        await mf.mushroom(client, message)

client.run(token_instance.token)
