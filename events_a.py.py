import nextcord
import random
from nextcord.ext import commands
#import asyncio
#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from datetime import datetime

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix= "$", help_command= None, intents=intents)



@bot.event
async def on_ready():
    print("Bot is online.")
    await bot.change_presence(status=nextcord.Status.dnd,activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Evil Intentions"))
@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        words = random.choice(["Howdy ", "Hey ", "Wassup "])
        if msg.content == "hello":
            await msg.channel.send(f"++ {words} {username} ")

@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Hi welcome to {guildname} !")

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)

    if emoji == "🕸️" and message_id == "enter your $messageid":
        role = nextcord.utils.get(guild.roles, name = "Spidey Fan")
        await member.add_roles(role)

    if emoji == "💜" and message_id =="enter your $messageid":
        role = nextcord.utils.get(guild.roles, name = "Venom Fan")
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)

    if emoji == "🕸️" and message_id =="enter your $messageid":
        role = nextcord.utils.get(guild.roles, name = "Spidey Fan")
        await member.remove_roles(role)

    if emoji == "💜" and message_id == "enter your $messageid":
        role = nextcord.utils.get(guild.roles, name = "Venom Fan")
        await member.remove_roles(role)

    
bot.run("Enter your bot token")

#joshwuznothere
