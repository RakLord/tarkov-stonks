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
        print(target.id)
        print("kick debug 3")
        await ctx.channel.send(f"Target: {target}")
        print("kick debug 4")
        await target.kick()
        log.clog(ctx)
        await log.dlog(ctx, self.bot)



def setup(bot):
	bot.add_cog(AdministrationCog(bot))