import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('Nzg3MDcwMjQ0ODU3NzA4NTk0.X9PmSQ.GVVlFHQpYlcpAPtfgTLugdFAi_A')