import discord
import requests
import json
import random

Client = discord.Client()

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
	"cheer up!",
	'Hang in there',
	'You are a great person'
]

def get_quote():
	response = requests.get("https://zenquotes.io/api/random")
	json_data = json.loads(response.text)
	quote = json_data[0]['q'] + " -" +json_data[0]['a']
	return quote

@Client.event
async def on_ready():
	print("Running....")
	print("We have logged in as {0.user}".format(Client))

@Client.event
async def on_message(message):
	if message.author == Client.user:
		return

	msg = message.content

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

	if message.content.startswith('$quote'):
		quote = get_quote()
		await message.channel.send(quote)

	if any(word in msg for word in sad_words):
		await message.channel.send(random.choice(starter_encouragements))

Client.run(Twink_Token)