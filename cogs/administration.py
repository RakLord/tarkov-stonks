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
        target = ctx.message.content[1:].split()[1:]
        target = target[0]
        target = bot.get_user(target)
        await ctx.send(target)
        await target.kick()
        log.clog(ctx)
        await log.dlog(ctx, self.bot)



def setup(bot):
	bot.add_cog(AdministrationCog(bot))