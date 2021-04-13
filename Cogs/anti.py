import discord 
import asyncio
from discord.utils import find
from discord.ext import commands, tasks

modules = [
    'role',
    'channel',
    'channel_del',
    'role_del',
    'ban',
    'kick',
    'bot',
    'role_update',
    'webhook_creation'
]


client = discord.Client()
client = commands.Bot(command_prefix='>', case_insensitive=True, intents=discord.Intents.all())
client.remove_command('help')


db = dontstealcodeClient.dont_stealcode("Universal").learn_tocode("servers")
db2 = dontstealcodeClient.dont_stealcode("Universal").learn_tocode("protection")

class UniversalSystem:

    def NewServer(owner_id, server_id):
        db.insert_one({
            "whitelisted": [578150206084874252, owner_id],
            "log": None,
            "punishment": "ban",
            "guild_id": server_id
        })
        db2.insert_one({
            "guild_id": server_id,
            "role": 'Enabled',
            "channel": 'Enabled',
            "channel_del": 'Enabled',
            "role_del": 'Enabled',
            "ban": 'Enabled',
            "kick": 'Enabled',
            "bot": 'Enabled',
            "role_update": 'Enabled',
            "webhook_creation": 'Enabled',
        })

@client.event
async def on_connect():
    os.system('cls')
    for server in client.guilds:
        if not db.find_one({ "guild_id": server.id }):
            guild_ = client.get_guild(server.id)
            UniversalSystem.NewServer(guild_.owner.id, guild_.id)
            print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m] Created DB For [\x1b[38;5;213m{server.name}\x1b[38;5;15m]')
    print(f'[\x1b[38;5;213mLOG\x1b[38;5;15m] Connected To [\x1b[38;5;213m{client.user}\x1b[38;5;15m]')
    watch = discord.Activity(type = discord.ActivityType.watching, name=f'>help')
    await client.change_presence(status=discord.Status.dnd, activity=watch)

@client.event
async def on_guild_join(guild):
    server = client.get_guild(guild.id)
    UniversalSystem.NewServer(server.owner.id, server.id)
    log_channel = client.get_channel(829624798882824213)
    embed = discord.Embed(title='Universal', color=0xf14645, description=f'Joined New Server!')
    embed.add_field(name='Server Name', value=f'**`{server.name}`**')
    embed.add_field(name='Server Owner', value=f'**`{server.owner}`**')
    embed.add_field(name='Server Members', value=f'**`{len(server.members)}`**')
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await log_channel.send(embed=embed)

@client.event
async def on_member_join(member):
    try:
        guild = member.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add).flatten()
        logs = logs[0]
        reason = "Adding Bot As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        await member.ban(f'Universal™ Premium | {reason}')
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await channel.send(embed=embed)
    except:
        pass 

@client.event
async def on_guild_role_update(before, after):
    try:
        guild = after.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_update).flatten()
        logs = logs[0]
        reason = "Updating Role As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass 

@client.event
async def on_webhook_update(webhook):
    try:
        guild = webhook.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.webhook_create).flatten()
        logs = logs[0]
        reason = "Bot Added As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        requests.delete(webhook)
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass 

@client.event
async def on_member_ban(guild, member):
    try:
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
        logs = logs[0]
        reason = "Banning Member As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        await guild.unban(user=logs.user.id)
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_member_kick(guild, member):
    try:
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.kick).flatten()
        logs = logs[0]
        reason = "Kicked Member As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_guild_role_delete(role):
    try:
        guild = role.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_delete).flatten()
        logs = logs[0]
        reason = "Bot Added As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_guild_channel_delete(channel):
    try:
        guild = channel.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_delete).flatten()
        logs = logs[0]
        reason = "Channel Deleted As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_guild_channel_create(channel):
    try:
        guild = channel.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.channel_create).flatten()
        logs = logs[0]
        reason = "Channel Created As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        await channel.delete()
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_guild_role_create(role):
    try:
        guild = role.guild
        logs = await guild.audit_logs(limit=1, action=discord.AuditLogAction.role_create).flatten()
        logs = logs[0]
        reason = "Role Created As Non-Whitelisted User"
        whitelisted = db.find_one({ "guild_id": guild.id })['whitelisted']
        if logs.user.id in whitelisted:
            return
        if client.user.id == logs.user.id:
            return
        await role.delete()
        punishment = db.find_one({ "guild_id": guild.id })['punishment']
        if punishment == 'ban':
            try:
                await logs.user.ban(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.ban(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        if punishment == 'kick':
            try:
                await logs.user.kick(reason=f"Universal™ Premium | {reason}")
            except:
                await guild.kick(discord.Object(logs.user.id), reason=f"Universal™ Premium | {reason}")
        channel = db.find_one({ "guild_id": guild.id })['log']
        if channel == None:
            pass
        else:
            log_channel = client.get_channel(channel)
            embed = discord.Embed(title='Universal', color=0xf14645)
            embed.description = 'Universal™ Premium'
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            embed.add_field(name='Banned', value=f'**`{logs.user}`**', inline=False)
            embed.add_field(name='Reason', value=f'**`{reason}`**', inline=False)
            await log_channel.send(embed=embed)
    except:
        pass    

@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    await ctx.send(embed=discord.Embed(color=0xf14645, timestamp=ctx.message.created_at, description=f'`{error}`'))

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645)
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    embed.add_field(name='General', value='**`botinfo`, `userinfo`, `serverinfo`, `members`, `invite`, `ping`**', inline=False)
    embed.add_field(name='Security', value=f'**`setup`, `toggle`, `settings`, `log`, `whitelist`, `punishment`, `whitelisted`, `unwhitelist`**', inline=False)
    embed.add_field(name='Moderation', value='**`ban`, `kick`, `unban`, `massunban`, `purge`, `nuke`**', inline=False)
    await ctx.channel.send(embed=embed)

# General

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title='Bot Information', color=0xf14645)
    embed.add_field(name='Name', value='`Universal`', inline=False)
    embed.add_field(name='Server Count', value=f'`{len(client.guilds)}`', inline=False)
    embed.add_field(name='User Count', value=f'`{len(set(client.get_all_members()))}`', inline=False)
    embed.add_field(name='Ping', value=f'`{int(client.latency * 1000)}`', inline=False)
    embed.add_field(name='Discord.py', value=f'`1.5.1`', inline=False)
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    if member == '':
        member = ctx.author
    embed = discord.Embed(title='User Info', color=0xf14645)
    embed.add_field(name="User ID", value=member.id, inline=False)
    embed.add_field(name="Name", value=member.display_name, inline=False)
    embed.add_field(name="Discriminator", value=member.discriminator, inline=False)
    embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
    embed.add_field(name="Bot Check", value=member.bot, inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(title='Server Info', color=0xf14645)
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Server Name", value=ctx.guild.name, inline=False)
    embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Creation Date", value=ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
    embed.add_field(name="Members", value=len(ctx.guild.members), inline=False)
    embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)  

@client.command()
async def members(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`{len(ctx.guild.members)}`**')
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645, description=f'[Click Here](https://discord.com/api/oauth2/authorize?client_id=777822336346488873&permissions=8&scope=bot)')
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`{int(client.latency * 1000)}`**')
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await ctx.send(embed=embed)

# Security

@client.command()
async def setup(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645)
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    embed.add_field(name='Commands', value='Type `>help` To Get A List Of My Available Commands.', inline=False)
    embed.add_field(name='Anti-Nuke', value=f'To Enable Universal\'s Protection Make Sure The `{client.user.name}` Role Is As High As Possible, Anyone Above The `{client.user.name}` Role Will Bypass Our Protection. Otherwise This Will Protect Your Server From Being Nuked, Wizzed, Destroyed The Anti-Nuke Module Is Automaticly Enabled, If You Wish To Turn Some Of Them Off Type `>toggle [MODULE]` To View All The Modules Type `>settings` I Hope You Enjoy.', inline=False)
    embed.add_field(name='Whitelisting', value='Type `>whitelist [@USER]` To Whitelist The User, Users That Are Whitelist Have The Ability To Bypass Our Protection So Be Carefull. Only The Server Owner Can Run This Command!', inline=False)
    await ctx.channel.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def toggle(ctx, module = None):
    if module == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Specify A Module To Toggle...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    if not module in modules:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Invalid Module To Disable**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        module_status = db2.find_one({ "guild_id": ctx.guild.id })[module.lower()]
        if module_status == 'Enabled':
            db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"{module.lower()}": 'Disabled'}})
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Disabled [{module.upper()}]`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)
        if module_status == 'Disabled':
            db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"{module.lower()}": 'Enabled'}})
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Enabled [{module.upper()}]`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def settings(ctx):
    embed = discord.Embed(title='Universal', color=0xf14645)
    embed.description = 'You Server Protection Settings'
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    punishment = db.find_one({ "guild_id": ctx.guild.id })['punishment']
    status = db2.find_one({ "guild_id": ctx.guild.id })['role']
    embed.add_field(name='Anti Role Creation', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`role`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['channel']
    embed.add_field(name='Anti Channel Creation', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`channel`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['channel_del']
    embed.add_field(name='Anti Channel Deletion', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`channel_del`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['role_del']
    embed.add_field(name='Anti Role Deletion', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`role_del`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['ban']
    embed.add_field(name='Anti Ban', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`ban`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['kick']
    embed.add_field(name='Anti Kick', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`kick`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['bot']
    embed.add_field(name='Anti Bot', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`bot`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['role_update']
    embed.add_field(name='Anti Role Update', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`role_update`**', inline=True)
    status = db2.find_one({ "guild_id": ctx.guild.id })['webhook_creation']
    embed.add_field(name='Anti Webhook Creation', value=f'Status: **`{status}`**\nPunishment: **`{punishment}`**\nAlias: **`webhook_creation`**', inline=True)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def log(ctx, channel = None):
    if channel == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Specify A Channel To Enable Logging On...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        channel_id = channel.split('<#')[1].split('>')[0]
        db.update_one({ "guild_id": ctx.guild.id }, { "$set": { "log": channel_id}})
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Updated Log Channel!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def whitelisted(ctx):
    if ctx.author.id == ctx.guild.owner.id:
        result = ''
        data = db.find_one({ "guild_id": ctx.guild.id })['whitelisted']
        for i in data:
            user_ = client.get_user(i)
            if user_ == None:
                user = 'Unable To Fetch Name'
            else:
                user = user_.name
            result += f"[{user}] :: {i}\n"
        with open(f'{ctx.guild.id}-Whitelisted.txt', 'a+') as f:
            f.write(result)
            f.close()
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Fetched Whitelisted Users`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed, file=discord.File(f'{ctx.guild.id}-Whitelisted.txt'))
        os.remove(f'{ctx.guild.id}-Whitelisted.txt')
    else:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Only {ctx.server.owner} Can Run This Command!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def unwhitelist(ctx, member: discord.Member = None):
    if ctx.author.id == ctx.guild.owner.id:
        if member == None:
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Specify A Member To Whitelist...`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)
        else:
            db.update_one({ "guild_id": ctx.guild.id }, { "$pull": { "whitelisted": member.id }})
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Unwhitelisted {member.name}`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Only {ctx.server.owner} Can Run This Command!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def whitelist(ctx, member: discord.Member = None):
    if ctx.author.id == ctx.guild.owner.id:
        if member == None:
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Specify A Member To Whitelist...`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)
        else:
            db.update_one({ "guild_id": ctx.guild.id }, { "$push": { "whitelisted": member.id}})
            embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Whitelisted {member.name}`**')
            embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Only {ctx.server.owner} Can Run This Command!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def punishment(ctx, punishment= None):
    if punishment == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Specify A Punishment...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    if punishment.lower() == 'ban':
        db.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "ban"}})
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Updated Punishment To Ban!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    elif punishment.lower() == 'kick':
        db.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "kick"}})
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Updated Punishment To Kick!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Invalid Punishment, Punishments Are Ban Or Kick!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

# Moderation

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=15):
    await ctx.channel.purge(limit=amount+1)

@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    channel_info = [ctx.channel.category, ctx.channel.position]
    await ctx.channel.clone()
    await ctx.channel.delete()
    new_channel = channel_info[0].text_channels[-1]
    await new_channel.edit(position=channel_info[1])

@client.command()
@commands.has_permissions(ban_members=True)
async def massunban(ctx):
    unbanned = 0
    banlist = await ctx.guild.bans()
    async for users in banlist:
        try:
            unbanned += 1
            await ctx.guild.unban(user=users.user)
            await asyncio.sleep(1)
        except:
            pass
    embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Unbanned {unbanned} Members!`**')
    embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.kick(reason=f'Kicked By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Kicked {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Provide A Member To Kick...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        await member.kick(reason=reason)
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Kicked {member} For {reason}.`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.ban(reason=f'Banned By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Banned {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Provide A Member To Ban...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        await member.ban(reason=reason)
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Banned {member} For {reason}.`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member_id = None):
    if member_id == None:
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Please Provide A Member ID To Unban...`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
    else:
        await ctx.guild.unban(user=member_id)
        embed = discord.Embed(title='Universal', color=0xf14645, description=f'**`Successfully Unbanned {member_id}!`**')
        embed.set_thumbnail(url='https://botuniversal.com/favicon-premium.png')
        await ctx.send(embed=embed)
