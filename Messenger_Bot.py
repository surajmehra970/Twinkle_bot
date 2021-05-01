import discord
import requests
import json
import random
import os

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

	if message.content.startswith('!help Twinkle'):
		await message.channel.send('You can use commands like !hello, !quote, !Case <country_name>')
	if message.content.startswith('!hello'):
		await message.channel.send('Hello!')

	if message.content.startswith('!quote'):
		quote = get_quote()
		await message.channel.send(quote)  

	if message.content.startswith('help'):
		await message.channel.send('use $help Twinkle')


	if any(word in msg for word in sad_words):
		await message.channel.send(random.choice(starter_encouragements))

	if message.content.startswith('!Case'):
		country = msg.split(' ')[1]
		response = requests.get('https://api.covid19api.com/total/country/'+country)
		json_data = json.loads(response.text)
		new_data = json_data[-1]
		Confirmed = new_data['Confirmed']
		Deaths = new_data['Deaths']
		Recovered = new_data['Recovered']
		Active = new_data['Active']
		await message.channel.send(f"Confirmed:{Confirmed}, Deaths:{Deaths}, Recovered:{Recovered}, Active:{Active}")

Client.run(os.environ['Twink_Token'])