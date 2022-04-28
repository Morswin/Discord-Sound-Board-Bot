# It's ok that it's not used yet. It will be eventually.
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='>')
# TOKEN loading stuff
# Forgive me for such defensive approach. 
# I don't want it to make the entire app to fail later.
try:
    with open("./token.txt") as file_containing_the_token:
        TOKEN: str = file_containing_the_token.readline()
        if TOKEN[-1] == '\n':
            TOKEN = TOKEN[:-1]
except:
    raise FileNotFoundError("It looks like the file with your TOKEN isn't where it should or is named incorrectly.")
try:
    assert len(TOKEN) >= 0
except:
    raise ValueError("TOKEN cannot be an empty String. Or can it?")
try:
    assert TOKEN[-1] != '\n'
except:
    raise ValueError("Failed to load the TOKEN.")


def main():
    # For now it's enough that this file exists.
    pass


if __name__ == "__main__":
    main()