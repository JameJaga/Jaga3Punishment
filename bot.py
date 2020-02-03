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
    channel = client.get_channel(663570894521761846)
    ban_users = await guild.bans()
    ban_count = len(ban_users)
    if message.author.bot:
        return
    #Helpコマンド
    elif message.content.startswith('/jphelp'):
        embed = discord.Embed(title="Jaga3PunishmentHelp",description="/jpmute {user}で{user}を発言禁止\n/jpkick　{user}で{user}をキック\n/jpban {user}で{user}をBAN",color=discord.Colour.blue())
        embed.add_field(name="**Perdon**",value="/jpunmute {user}で{user}の発言禁止解除\n/jpperdon {user}で{user}のBAN解除。")
        await message.channel.send(embed=embed)
        await channel.send(embed=embed)
        return
    #Kickコマンド
    elif message.content.startswith('/jpkick'):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            await guild.kick(user=member)
            embed = discord.Embed(title="MemberKicked",description = f'{str(member)}をキックしました。',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command.',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
    #muteコマンド
    elif message.content.startswith('/jpmute'):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            role = discord.utils.get(message.guild.roles, name='Muted')
            await member.add_roles(role)
            embed = discord.Embed(title="MemberMuted",description = f'{str(member)}をミュートしました。',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
    #unmuteコマンド
    elif message.content.startswith('/jpunmute'):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            role = discord.utils.get(message.guild.roles, name='Muted')
            await member.remove_roles(role)
            embed = discord.Embed(title="MemberUnmuted",description = f'{str(member)}のミュートを解除しました。',color=discord.Colour.from_rgb(255, 0, 247))
            await message.channel.send(embed=embed)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
    #banコマンド
    elif message.content.startswith('/jpban'):
        if message.author.guild_permissions.administrator:
            member = message.mentions[0]
            await guild.ban(user=member)
            embed = discord.Embed(title="MemberBanned",description = f'{str(member)}をBANしました。',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(title="AccessDenied",description = 'You do not have permisson to use this command',color=discord.Colour.from_rgb(255, 0, 0))
            await message.channel.send(embed=embed)
    #処罰中の人数を表示する。
    #これBANの表示
    ChannelName = f'BANNED:{str(ban_count)}'
    VoiceChannel = client.get_channel(672694655502254080)
    await VoiceChannel.edit(name=ChannelName)
    #これmuteの表示
    role = discord.utils.get(message.guild.roles, name='Muted')
    Mute_count = len(role.members)
    ChannelName = f'Muted:{str(Mute_count)}'
    VoiceChannel = client.get_channel(672694696946171914)
    await VoiceChannel.edit(name=ChannelName)
client.run(TOKEN)
