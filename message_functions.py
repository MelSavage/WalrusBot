import discord
import asyncio
from random import choice

# Message responses

async def ping(client, message):
    await client.send_message(message.channel, 'Pong!')

async def mushroom(client, message, image_picker):
    image_path = await image_picker.select_image('shroom', 58)
    with open(image_path, 'rb') as f:
        await client.send_file(message.channel, f)

async def walrus(client, message, image_picker):
    image_path = await image_picker.select_image('walrus', 47)
    with open (image_path, 'rb') as f:
        await client.send_file(message.channel, f)

async def angry8ball(client, message):
    if len(message.content) > 11:
        answer = await eight_ball_answer()
        await client.send_message(message.channel, answer)
    else:
        answer = "Ask me a question starting with %angry8ball and I will " + \
        "respond in a sarcastic or dismissive manner!"
        await client.send_message(message.channel, answer)

# Supporting functions

async def eight_ball_answer():
    answers = (("It is certain. Now leave me alone!", "It is decidedly " +
            "so, jackass!", "Yes. What the fuck do you think?!?",
            "Reply hazy. Don't ask me again!", "Ask again... never!",
            "Concentrate, but not too hard, you'll hurt something. Then ask " +
            "again?", "My reply is no. What the fuck do I care?!?", "Outlook "
            + "as negative as your shitty life.", "Just stop now, you're " +
            "full of shit."))
    return choice(answers)
