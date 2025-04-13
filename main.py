# This example requires the 'message_content' intent.
import os
import sys
import discord
import requests
import datetime
import pathlib
from typing import Final
from dotenv import load_dotenv


class MyClient(discord.Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.WEATHER_TOKEN: Final[str] = os.getenv('WEATHER_TOKEN')

    async def on_ready(self):
        
        print(f'Logged on as {self.user}!')

        date = datetime.datetime.now()

        try:    
            channel = self.get_channel(1248670152145371258)  # Use an integer, not a string
            data = get_weather(self.WEATHER_TOKEN)
            
            if not self.WEATHER_TOKEN:
                raise ValueError("Weather token not set or found.")

            myid = "<@415334022214844418>"
            await channel.send(f"{myid} {data['location']['name']}: {data['current']['temp_c']}°C as of {date}")
            await self.close()
        except Exception as e:
            if channel:
                await channel.send(f"Error occurred: {e}")
            else:
                print(f"Failed to find channel: {e}")

        return 1


def get_weather(WEATHER_TOKEN):
    r = requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_TOKEN}&q=Toronto&aqi=no')
    data = r.json()
    return data


def main():
    script_directory = pathlib.Path(__file__).resolve().parent
    dotenv_path = script_directory / ".env"

    load_dotenv(dotenv_path)
     
    # place the token in a .env file and import the token below    
    DISC_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents) 

    client.run(DISC_TOKEN)

    sys.exit()


main()
