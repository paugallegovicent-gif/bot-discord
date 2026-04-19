import discord
import random
import asyncio

# Define the client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Define the custom prizes and animations
prizes = ["$10 Gift Card", "$20 Gift Card", "$50 Gift Card", "Custom Emoji", "VIP Role"]
animations = [
    "🎉 Spinning... 🎉",
    "🤑 Rolling... 🤑",
    "🤩 Winning... 🤩"
]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!roulette'):
        await play_roulette(message.channel)

async def play_roulette(channel):
    animation_message = await channel.send(random.choice(animations))
    await asyncio.sleep(2)  # Simulate delay for animation

    prize = random.choice(prizes)
    await channel.send(f'You won: {prize}!')
    await animation_message.delete()  # Remove animation message

# Run the Discord bot
client.run('YOUR_BOT_TOKEN')