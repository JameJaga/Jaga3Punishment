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
    guild = message.guild
    if message.author.bot:
        return
    #Helpコマンド
    if message.content == '/jphelp':
        embed = discord.Embed(title="Jaga3PunishmentHelp",description="/jpmute {user}で{user}を発言禁止\n/jpkick　{user}で{user}をキック\n/jpban {user}で{user}をBAN",color=discord.Colour.blue())
        embed.add_field(name="**Perdon**",value="/jpunmute {user}で{user}の発言禁止解除\n/jpperdon {user}で{user}のBAN解除。")
        await message.channel.send(embed=embed)
    
    #Kickコマンド
    if message.content.startswith('/jpkick'):
        member = message.mentions[0]
        await guild.kick(user=member)
        embed = discord.Embed(title="MemberKicked",description = f'{str(member)}をキックしました。',color=discord.Colour.from_rgb(255, 0, 0))
        await message.channel.send(embed=embed)
        
    #muteコマンド
    if message.content.startswith('/jpmute'):
        member = message.mentions[0]
        role = discord.utils.get(message.guild.roles, name='Muted')
        await member.add_roles(role)
        embed = discord.Embed(title="MemberMuted",description = f'{str(member)}をミュートしました。',color=discord.Colour.from_rgb(255, 0, 0))
        await message.channel.send(embed=embed)
        
    #unmuteコマンド
    if message.content.startwith('/jpunmute'):
        member = message.mentions[0]
        role = discord.utils.get(message.guild.roles, name='Muted')
        await member.remove_roles(role)
        embed = discord.Embed(title="MemberUnmuted",description = f'{str(member)}のミュートを解除しました。',color=discord.Colour.from_rgb(255, 0, 247))
        await message.channel.send(embed=embed)
        
    #banコマンド
    if message.content.startswith('/jpban'):
        member = message.mentions[0]
        await guild.ban(user=member)
        embed = discord.Embed(title="MemberBanned",description = f'{str(member)}をBANしました。',color=discord.Colour.from_rgb(255, 0, 0))
        await message.channel.send(embed=embed)
client.run(TOKEN)
