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
        print("Kick debug 1")
        # target = ctx.message.mentions
        print("kick debug 2")
        await ctx.send(f"Target: `{user}`")
        print("kick debug 3")
        await ctx.kick(user)
        log.clog(ctx)
        await log.dlog(ctx, self.bot)
        print("kick debug 4")



def setup(bot):
	bot.add_cog(AdministrationCog(bot))