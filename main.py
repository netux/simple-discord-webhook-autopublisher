import discord
from configparser import ConfigParser

if __name__ == "__main__":
	config = ConfigParser()
	config.read("config.ini")

	client = discord.Client(intents=discord.Intents.default())

	@client.event
	async def on_message(msg: discord.Message):
		if (msg.webhook_id == config["config"]["webhook_id"]):
			await msg.publish()

	client.run(token=config["config"]["token"])
