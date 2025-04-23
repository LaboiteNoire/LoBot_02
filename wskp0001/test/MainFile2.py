"""
Main Class File
"""
import discord
from discord.ext import commands
import random
from discord.ext import commands
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import os
import TypographieFile as tf
nonetxt = "᲼"


bot = commands.Bot(command_prefix = "°", description = "Ceci n'est pas le lolabot , toute ressemblance avec le lolabot est purement fortuite")
slash = SlashCommand(bot, sync_commands=True)
@bot.event
async def on_ready():
	print("NotLolaBot online")
	await bot.change_presence(activity=discord.Game(name="°help"))




@bot.command()
async def say(ctx, *txt):
        """partager la sainte parole du non lola bot"""
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send(" ".join(txt))
@bot.command()
async def register(ctx):
        """register command"""
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id 
        select = tf.getListSelection(ctx,"chose the register",["competence","test"],["competence","test"]) 
        fait_choix = await ctx.send("`Chose the register : `", components=[create_actionrow(select)])
        print("ok")
        typage = await wait_for_component(bot, components=select, check=check)
        Type = typage.values[0]
        await typage.send(nonetxt)







bot.run("MTEzMzA0NzYzMTg0OTk5MjMyNQ.GIM64A.IF16b8ccriPbkJvjWyETL4tAeOJ-53AvsbKqTk")
