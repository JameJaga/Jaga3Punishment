import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()
num = 0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):     
    if message.content == '/jphelp':
        embed = discord.Embed(title="Jaga3PunishmentHelp",description="/jpmute {user}で{user}を発言禁止\n/jpkick　{user}で{user}をキック\n/jpban {user}で{user}をBAN",color=0xff0000)
        embed.add_field(name="perdon",value="/jpunmute {user}で{user}の発言禁止解除 /jpperdon {user}で{user}のBAN解除。")
        await message.channel.send(embed=embed)
    
client.run(TOKEN)
