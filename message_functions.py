import discord
import asyncio

async def ping(client, message):
    await client.send_message(message.channel, 'Pong!')

async def mushroom(client, message):
    with open('images/shroom/1.jpg', 'rb') as f:
        await client.send_file(message.channel, f)
