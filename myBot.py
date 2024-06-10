import discord
from discord.ext import commands
import dotenv
import os
from PyDiscoBot import commands
from MLEBot import mle_commands, mle_bot


class MyBot(mle_bot.MLEBot):
    def __init__(self,
                 command_prefix: str | None = None,
                 bot_intents: discord.Intents | None = None,
                 command_cogs: [discord.ext.commands.Cog] = None):
        super().__init__(command_prefix=command_prefix,
                         bot_intents=bot_intents,
                         command_cogs=command_cogs)


if __name__ == '__main__':
    dotenv.load_dotenv()

    intents = discord.Intents(8)
    # noinspection PyDunderSlots
    intents.guilds = True
    # noinspection PyDunderSlots
    intents.members = True
    # noinspection PyDunderSlots
    intents.message_content = True
    # noinspection PyDunderSlots
    intents.messages = True
    # noinspection PyDunderSlots
    intents.reactions = True

    bot = MyBot('ub.',
                intents,
                [commands.Commands,
                 mle_commands.MLECommands])

    bot.run(os.getenv('DISCORD_TOKEN'))
