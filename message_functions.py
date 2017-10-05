import discord
import asyncio
from random import randint

async def ping(client, message):
    await client.send_message(message.channel, 'Pong!')

async def mushroom(client, message):
    image_path = image_picker('shroom', 58)
    with open(image_path, 'rb') as f:
        await client.send_file(message.channel, f)

def image_picker(folder, num_pictures):
    """
    Generate address for image dynamically. Needs subfolder name and
    number of pictures arguments
    """
    pic_num = randint(1, num_pictures)
    image_path = "images/" + folder + "/" + str(pic_num) + ".jpg"
    return image_path
