#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from discord.ext import commands
import discord, asyncio, time

TOKEN = "" # colocar el token

pr = discord.ext.commands.bot
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return

#         if message.content == 'ping':
#             await message.channel.send('pong')


#client = MyClient(intents=intents)
client = commands.Bot(command_prefix="", description="", intents=intents ) # colocar el prefijo (obligatorio) y la descripcion (opcional)

@client.command()
async def test(ctx):
    await ctx.send("Hello world!") # comando de prueba

# comandos
@client.command()
async def say(ctx, *, text):
    await ctx.send(text)
    await ctx.message.delete() # repite lo que dijo el usuario que ejecuto el comando y elimina su mensaje

@client.command()
async def purge(ctx, arg:int):
	await ctx.channel.purge(limit=arg) # elimina x mensajes (limite 1000)

@client.command(pass_context=True)
async def create_role(ctx, name):
    guild = ctx.guild
    await guild.create_role(name=name) # crea un rol nuevo a partir del nombre

@client.command(pass_context=True)
async def create_channel(ctx, name):
    guild = ctx.message.guild
    await guild.create_text_channel(name) # crea un canal a partir de su nombre

@client.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete() # banea a un usuario a partir de su nombre o de su id

# events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Minecraft"))
    print("Ready!!!!") # cuando el bot se active, imprimira ready!!!!

# filtrador de palabras
@client.event
async def on_message(ctx, message):
    msg = message.content

    with open('badWords.txt') as BadWords:
        if msg in BadWords.read():
            await message.delete()
            await ctx.send("") # colocar el mensaje de warn
        else:
            await ctx.process_commands(message)

client.run(TOKEN)
