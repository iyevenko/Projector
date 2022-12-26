import discord
import os
import sys

import ffmpy

BOT_TOKEN = os.getenv('BOT_TOKEN')
GENERAL_CHANNEL_ID = 1056727504339091651

intents = discord.Intents()
intents.messages = True
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)

gifs = []

@client.event
async def on_ready():
	channel = client.get_channel(GENERAL_CHANNEL_ID)

	async for message in channel.history(limit=None):
		if message.attachments:
			attachment = message.attachments[0]

			if attachment.filename.endswith(('.jpg', '.png', '.gif')):
				response = await attachment.read()

				path = './content/' + attachment.filename
				open(path, 'wb').write(response)

				path, ext = os.path.splitext(path)
				if ext == '.gif':
					gifs.append(path)


	await client.close()


client.run(BOT_TOKEN)


for path in gifs:
	ff = ffmpy.FFmpeg(
		inputs={path+'.gif': None},
		outputs={path+'.mp4': None}
	)
	ff.run()
	os.remove(path+'.gif')