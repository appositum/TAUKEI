import asyncio
import discord
import os

token = os.environ.get('DISCORD_BOT_SECRET')

client = discord.Client()

@client.event
async def on_ready():
    print("Im ready oh yeaah")
    await client.change_presence(game=discord.Game(name="Anemonas is beautiful"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "oi":
        await client.send_message(message.channel, "Mano namoral o Anemonas me criou então cala a boquita aí por favor. Obrigado")
    elif message.content == "alex":
        await client.send_message(message.channel, "VOCÊ DISSE ALEX???? AQUELE LINDO??? ``AGR PABLLO VITTAR FOI MUITO LONGE QUANDO DISSE ISSO`` :sunglasses:	PSE ")
    elif message content == "admin":
	await client.send_message(message.channel, "RESPEITAR O ADMIN OK?")		
client.run(token)
