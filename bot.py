import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import google.generativeai as aimodel

# takes keys from the .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SYSTEM_INSTRUCTIONS = os.getenv("SYSTEM_INSTRUCTIONS")

# do the ai thingy
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# get like scopes or whatever theyre called
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user} we up gng")
@bot.command()
async def ping(ctx):
	await ctx.send("Pong!")

@bot.event 
async def on_message(message):
	if message.aither.bot:
		returm
	#ignore commands like !ping
	await bot.process_commands(message)
	#send die message to daddy google
	prompt = f""
SYSTEM INSTRUCTIONS:
{SYSTEM_INSTRUCTIONS}
USER MESSAGE:
{message.content}
"""

	try:
		response = model.generate_content(prompt)
		reply_text = response.text[:2000] # LOL discord actually does max out to 2000 chars
		await message.channel.send(reply_text)
	except Exception as e:
		print("im bugging bro look at ts:", e)
		await message.channel.send("friggin google aint telling me what to say bro")
bot.run(DISCORD_TOKEN)