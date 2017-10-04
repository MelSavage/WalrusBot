import discord
import asyncio

async def ping(client, message):
    await client.send_message(message.channel, 'Pong!')
