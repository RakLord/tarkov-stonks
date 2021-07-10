import discord
import os
from discord.ext import commands
from utils import log


# Hope you enjoy messy bad code :)
# Testing updates
# # # # # # # # # # # # # # #


# Get bot token 
f = open("TOKEN.txt", "r")
TOKEN = f.read()
# # # # # # # # # # # # # # #


# Initial config (maybe move to file later?)
prefixes = [".", "!", "?", ","]


def get_prefix(bot, message):
    if not message.guild:
        return "!" # Only allow ! to be used in DM's
    
    return commands.when_mentioned_or(*prefixes)(bot, message)


log_channel_id = 862731162808090654

# # # # # # # # # # # # # # # 


# Other stuff
initial_extensions = ['cogs.administration',
                      'cogs.tarkov']


# # # # # # # # # # # # # # #


bot = commands.Bot(command_prefix=get_prefix, description="Tarkov Market Bot")


if __name__ == "__main__":
    for extension in initial_extensions:
        print(f"DEBUG: Loading {extension}")
        bot.load_extension(extension)

        

def format_print(print_text, width):
    if ((width - len(print_text)) % 2) == 0:
        spacer_len = round((width - len(print_text)) / 2)
        spacer = "#"*spacer_len
        text_spaced = spacer + print_text + spacer
        return text_spaced

    else:
        spacer_len = round((width - len(print_text)) / 2)
        spacer = "#"*spacer_len
        spacer1 = "#"*spacer_len + "#"
        text_spaced = spacer + print_text + spacer1
        return text_spaced





@bot.event
async def on_ready():
    os.system("clear")
    con_format_len = 35
    print(format_print("#"*con_format_len, con_format_len))
    print(format_print(" "*30, con_format_len))
    print(format_print("   Tarkov Stonks   ", con_format_len))
    print(format_print(" "*30, con_format_len))
    print(format_print("#"*con_format_len, con_format_len))
    print(format_print(" "*30, con_format_len))
    print(format_print("     Created     ", con_format_len))
    print(format_print("     By:     ", con_format_len))
    print(format_print("   Shaeca16   ", con_format_len))
    print(format_print(" "*30, con_format_len))
    print(format_print("#"*con_format_len, con_format_len))
    print("")


    presence = discord.Game("Tarkov Stonks")
    await bot.change_presence(status=discord.Status.online, activity=presence)

    await log.d_sys_log()
    print("DEBUG: Bot Online.")



ignored_errors = (commands.CommandNotFound, )

@commands.Cog.listener()
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, ignored_errors):
        return

    elif isinstance(error, commands.NoPrivateMessage):
        log.clog(ctx, True)



bot.run(TOKEN, bot=True, reconnect=True)
