import os
from dotenv import load_dotenv
import discord

load_dotenv() 
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
log_channel = None


@client.event
async def on_ready():
    global log_channel
    global client
    print(f'We have logged in as {client.user}')
    log_channel = discord.utils.get(client.get_all_channels(), name='nsfw-sexting-room-1')

@client.event
async def on_message(message):
    global log_channel
    if message.author == client.user:
        return

    if message.channel.type == discord.ChannelType.private:
        if len(message.attachments):
            file = await message.attachments[0].to_file()
            await log_channel.send("A file was sent", file=file)
            print('sent file to log_channel...')

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(token)
