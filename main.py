import os
import asyncio
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# loading token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup (activate intents/permission)
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)


# Functions
async def send_message(message: Message, username: str, user_message: str) -> None:
    if not user_message:
        print('Bot message')
        return
    if user_message[0] == '+':
        user_message = user_message[1:]
        try:
            response = await asyncio.to_thread(get_response, user_message, username)
            await message.channel.send(response)
        except Exception as e:
            print(e)


# Handling startup
@client.event
async def on_ready() -> None:
    print(f'({client.user} is now running!)')


# Handling messages
@client.event
async def on_message(message) -> None:
    if message.author == client.user:
        return
    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    # print(f'[{channel}] {username}: "{username}"')
    await send_message(message, username, user_message)


# main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
