import discord
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')


intents = discord.Intents()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
	# Check if the message contains an attachment
	if message.attachments:
	    # Get the first attachment in the list of attachments
	    attachment = message.attachments[0]
	    # Check if the attachment is an image (jpg, png, or gif)
	    if attachment.filename.endswith(('.jpg', '.png', '.gif')):
	        # Download the image and save it to a local folder
	        response = await attachment.read()
	        open('./content/' + attachment.filename, 'wb').write(response)

client.run(BOT_TOKEN)
