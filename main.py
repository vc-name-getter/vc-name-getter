import discord
from discord.ext import commands
from keep_alive import keep_alive
import os

# Define the intents
intents = discord.Intents.all()
# intents.members = True  # Enable the members intent to access members in voice channels
# intents.voice_states = True  # Enable the voice states intent to access voice channel info

# Create an instance of a bot with a command prefix and intents
bot = commands.Bot(command_prefix=';', intents=intents)


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author}!")


@bot.command()
async def get_vc_members(ctx):
    print("Command invoked")
    # Get the author's voice channel
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None

    if voice_channel is None:
        await ctx.send("You are not in a voice channel!")
        return

    # Get the members in the voice channel
    members = voice_channel.members

    if len(members) == 0:
        await ctx.send("There is no one in the voice channel.")
    else:
        # Create a string with @ symbols before the actual Discord username (not nickname)
        mentions = ", ".join([f"@{member.name}" for member in members])
        await ctx.send(f"\n {mentions}")


# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    print('Ready to go!')


# Start the keep-alive web server
keep_alive()

# Run the bot with your token
bot.run(os.getenv('MTI4OTc5OTgyNTgzNTE2Nzc3NA.Gki-5R.84K0zKRhiOtSJz1Ks3eWXDh_TDZed-YxteRZb0'))
