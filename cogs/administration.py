import discord
from discord.ext import commands
from utils import log


class AdministrationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True) 
    async def kick(self, ctx):
        print("Kick debug 1")
        target = ctx.message.mentions
        print(target)
        print("kick debug 3")
        await ctx.send(f"Target: {target}")
        print("kick debug 4")
        await ctx.guild.kick(target)
        log.clog(ctx)
        await log.dlog(ctx, self.bot)
        print("kick debug 5")



def setup(bot):
	bot.add_cog(AdministrationCog(bot))