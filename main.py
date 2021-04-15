import discord
import os
import requests
import json


client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" #json_data[0]['a']
  return(quote)

@client.event
async def on_ready(): #when the bot is ready
    print("we have logged in as {0.user}.format(client)")


@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('$Hello'):
      await message.channel.send("Hello!")

    if message.content.startswith("$inspire"):
      quote = get_quote()
      await message.channel.send(quote)

    if message.content.startswith("$gay"):
      await message.channel.send("nice")

    if message.content.startswith("I love you bot"):
      await message.channel.send("*blushing*")


client.run(os.getenv('TOKEN'))
