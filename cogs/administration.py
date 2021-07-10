import discord
from discord.ext import commands
from utils import log


class AdministrationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True) 
    async def kick(self, ctx, user: discord.Member):
        await ctx.guild.kick(user)
        await ctx.send(f"**Kicked:** `{user}`")
        await user.send(f"**You were kicked from:** {ctx.guild.name}")
        await log.dlog(ctx, self.bot)


def setup(bot):
	bot.add_cog(AdministrationCog(bot))
