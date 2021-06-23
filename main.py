from discord.ext import commands
import random



bot = commands.Bot(command_prefix="",case_insensitive=True)

@bot.event
async def on_ready():
    print("\n Logged in as: " + bot.user.name)
    

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.lower().startswith("towa"):
            f = open("link.txt", "r")
            split = f.read().split("\n")

            rand = random.randint(0, len(split) -1)
            await message.channel.send(split[rand])

        elif message.content.lower().startswith("addlink"):
            split = message.content.split(" ") # [1] -> link
            file = open("link.txt", "a")
            text = "\n" + split[1]
            file.write(text)
            await message.delete()
            await message.channel.send(f"Successfully added link!", delete_after=5)
            file.close()


bot.run("TOKEN")
