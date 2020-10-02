import discord
from discord.ext import commands

from util.decorators import delete_original


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @delete_original()
    async def ping(self, ctx):
        """Latency of the bot"""
        await ctx.send(f":ping_pong: Pong! {str(round(self.bot.latency * 1000, 0))[:2]}ms :signal_strength:")


def setup(bot):
    bot.add_cog(Utility(bot))
