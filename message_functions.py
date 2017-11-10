import discord
import asyncio
from random import choice

# Message responses

async def ping(client, message):
    await client.send_message(message.channel, 'Pong!')

async def mushroom(client, message, image_picker):
    image_path = await image_picker.select_image('shroom')
    with open(image_path, 'rb') as f:
        await client.send_file(message.channel, f)

async def walrus(client, message, image_picker):
    image_path = await image_picker.select_image('walrus')
    with open (image_path, 'rb') as f:
        await client.send_file(message.channel, f)

async def banana(client, message, image_picker):
    image_path = await image_picker.select_image('banana')
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

async def emote(client, message):
    if len(message.content) > 7:
        image_path = await emote_image(message)
        if image_path:
            with open (image_path, 'rb') as f:
                await client.send_file(message.channel, f)
    else:
        answer = ("Say %emote followed by one of the following commands: " +
                  "angry, concerned, diva, fail, hungry, love, rofl, sad, " +
                  "ugh, welcome, yay.")
        await client.send_message(message.channel, answer)

async def aubergine(client, message):
    await client.add_reaction(message, '\U0001F923')
    fmt = 'Very funny, {0.mention}!'
    await client.send_message(message.channel, fmt.format(message.author))

async def help(client, message, settings):
    fmt = "I can respond to the following commands.\n" + \
             "{0}mushroom, {0}walrus, {0}angry8ball, {0}emote, {0}banana"
    await client.send_message(message.channel, fmt.format(settings.prefix))

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

async def emote_image(message):
    emote = message.content[7:]
    possible_emotes = ["angry", "concerned", "diva", "fail", "hungry", "love",
        "rofl", "sad", "ugh", "welcome", "yay"]
    if emote in possible_emotes:
        image_path = ".\\images\\emote\\" + emote + ".jpg"
        return image_path
    else:
        return None
