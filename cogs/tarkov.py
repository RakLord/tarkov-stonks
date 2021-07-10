import discord
from discord.ext import commands
from utils import log


class TarkovCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def search(self, ctx):
        await ctx.send("Feature WIP")
        await log.dlog(ctx, self.bot)


def setup(bot):
    bot.add_cog(TarkovCog(bot))
