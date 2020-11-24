# https://discord.com/api/oauth2/authorize?client_id=772081109969666058&permissions=0&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D772081109969666058%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscord.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D772081&scope=bot
import discord
from discord.ext import commands

import json
import requests
from random import randint

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send('Pong')

@bot.command()
async def do(ctx, what :str, *args :str):
    if (what == 'math' and len(args) == 3):
        if (str(args[1]) == '+'):
            await ctx.send(float(args[0]) + float(args[2]))
        elif (str(args[1]) == '-'):
            await ctx.send(float(args[0]) - float(args[2]))
        elif (str(args[1]) == '*'):
            await ctx.send(float(args[0]) * float(args[2]))
        elif (str(args[1]) == '/'):
            await ctx.send(float(args[0]) / float(args[2]))
        elif (str(args[1] == '**')):
            await ctx.send(float(args[0]) ** float(args[2]))
    elif (what == 'random' and args[0]):
        await ctx.send(randint(0, int(args[0])))


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@bot.command()
async def pika(ctx):
    response = requests.get('https://some-random-api.ml/img/pikachu')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xffe840, title = 'Random Pika-pika-chuuuuu!!!')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

bot.run('NzcyMDgxMTA5OTY5NjY2MDU4.X51ekQ.yScrUMh_RS2eYKkybjCSGbSw7Qc')