import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def 반복(ctx, 횟수: int, *, 내용: str):
    횟수 = min(max(횟수, 1), 10)

    for _ in range(횟수):
        await ctx.send(내용)
        await asyncio.sleep(2)

bot.run(os.environ["DISCORD_TOKEN"])
