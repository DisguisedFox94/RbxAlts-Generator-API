import discord,json,random,string,time,os,aiohttp,requests
from colorama import Fore
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter
from bs4 import BeautifulSoup
prefix = "-"
autoAPI = True
with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
prefix = config.get('prefix')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, self_bot=True)
@bot.event
async def on_ready():
    os.system('cls')
    print(f"""

{Fore.RED}█████▀████████████████████████████████████████████████████████████████████
{Fore.GREEN}█─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─▄▄▀██▀▄─██─▄─▄─█─▄▄─█▄─▄▄▀████▀▄─██▄─▄▄─█▄─▄█
{Fore.RED}█─██▄─██─▄█▀██─█▄▀─███─▄█▀██─▄─▄██─▀─████─███─██─██─▄─▄████─▀─███─▄▄▄██─██
{Fore.GREEN}▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▀{Fore.WHITE}

Generator API by: Disguised Fox
This is souly for RbxAlts discord server, Xyba didn't give me permission to do this
Use {Fore.RED}-gen{Fore.WHITE} anywhere!
""")
@bot.command()
async def api(ctx):
    channel = bot.get_channel(768628142662352907)
    delay = channel.slowmode_delay
    await channel.send('-gen')
    await ctx.send(f'Account Generated! Check your DMs with **RBXALTS Premium**\n\nYour on a {delay} second cooldown, Please wait.')
    time.sleep(delay)
    async with aiohttp.ClientSession() as session:
        webhook = config.get('webhook')
        webhook = Webhook.from_url({webhook}, adapter=AsyncWebhookAdapter(session))
        await webhook.send(f"<@!{bot.user.id}>, Cooldown's over.")
@bot.command()
async def auto_api(ctx):
    autoAPI = True
    await ctx.send("Possible may get you banned.\n\n*Activated Auto API*.")
    if autoAPI == True:
        while True:
            channel = bot.get_channel(768628142662352907)
            delay = channel.slowmode_delay
            await channel.send('-gen')
            print(f'Account Generated! Check your DMs with **RBXALTS Premium**\n\nYour on a {delay} second cooldown, Please wait.')
            time.sleep(delay)
            print(f'{bot.user} {delay} second cooldown is over.')
@bot.command()
async def disable_api(ctx):
    autoAPI = False
    await ctx.send("Auto API was disabled, use `-auto_api` to enable it.")
bot.run(token, bot=False)
