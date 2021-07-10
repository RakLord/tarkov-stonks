import discord
from discord.ext import commands
from datetime import date


def clog(ctx, dm=False):  # Console log for command usage
	if not dm:
		print(f"\nDEBUG:\n-> User: {ctx.author}",
			f"\n-> Server: {ctx.message.guild.name}",
			f"\n-> Action: {ctx.message.content[1:].split()[0]}",
			f"\n-> Args: {', '.join(ctx.message.content[1:].split()[1:])}\n",
			"#"*32)
	else:
		print(f"\nDEBUG:\n-> User: {ctx.author}",
			f"\n-> Action: {ctx.message.content[1:].split()[0]}",
			f"\n-> Server: DM's",
			f"\n-> Args: {', '.join(ctx.message.content[1:].split()[1:])}\n",
			"#"*32)	



async def dlog(ctx, bot, dm=False):  # Discord log, only for command usage
	log_channel = bot.get_channel(862731162808090654)
	embed_user = ctx.author
	embed_action = ctx.message.content[1:].split()[0]
	embed_args = ", ".join(ctx.message.content[1:].split()[1:])
	if not embed_args:
		embed_args = "None"
	print(dm)
	if not dm:
		print("DM False")

		embed_guild = ctx.guild.name
		embed_var = discord.Embed(title="[ Tarkov-Stonks-Logs ]")
		today = date.today().strftime("%b-%d-%Y")
		embed_var.set_footer(text=today)
		embed_var.add_field(name="**User:** ", value=embed_user, inline=False)
		embed_var.add_field(name="**Guild:** ", value=embed_guild,inline=False)
		embed_var.add_field(name="**Action:** ", value=embed_action,inline=False)
		embed_var.add_field(name="**Args:** ", value=embed_args,inline=False)
		await log_channel.send(embed=embed_var)

	else:
		print("Dm True")


async def d_sys_log(bot, msg):
	log_channel = bot.get_channel(862731162808090654)
	embed_var = discord.Embed(title="[ System Log ]")
	today = date.today().strftime("%b-%d-%Y")
	embed_var.set_footer(text=today)
	embed_var.add_field(name="**LOG: **", value=msg, inline=False)
	log_channel.send(embed=embed_var)