from decouple import config
from interactions import (SlashContext, OptionType, Client, SlashCommand,
                          slash_option, SlashCommandChoice, AutocompleteContext, listen)
from api_requests import get_request, post_request, put_request, delete_request
import os
from json import dump as json_dump


@listen()
async def on_ready():
    """Lets the console know when the bot is online."""
    print("Ready")
    print(f"This bot is owned by {bot.owner}")

    # Make sure the database file is already there. If it's not, create it
    if not os.path.isfile(config("FILENAME")) or not os.path.isfile(config("FILENAME")):
        with open(config("FILENAME"), 'w') as new_json:
            json_dump({"users": {}}, new_json)


base_command = SlashCommand(
    name="eyebot",
    description="Tool to query apis"
)

# -------------------------------------------------------------------------------------------------------------------- #
"""get"""


@base_command.subcommand(sub_cmd_name="get", sub_cmd_description="Query an api")
@slash_option(name="api_url", description="Provide an endpoint", opt_type=OptionType.STRING, required=True)
@slash_option(name="show_everyone", description="Make response visible to all", opt_type=OptionType.BOOLEAN, required=False)
async def get(ctx: SlashContext, api_url, show_everyone=False):
    reply = get_request(api_url)
    # sort by id if id exists
    sorted_reply = sorted(reply, key=lambda x: x.get('id', float('inf')) if isinstance(x, dict) else float('inf'))
    await ctx.send(str(sorted_reply), ephemeral=not show_everyone)


if __name__ == "__main__":
    # Set the cwd to the directory where this file lives
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Define and start the bot
    bot = Client(token=config("BOT_TOKEN"))
    bot.start()
