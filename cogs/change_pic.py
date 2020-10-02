import os
import datetime

import asyncio
import discord
from discord.ext import commands

from util.logger import Logger
from util.decorators import delete_original
from util.config import BotConfig


class Background(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = BotConfig().data
        self.prev_img = ""

        self.bot.loop.create_task(self.image_loop())

    # @commands.Cog.listener("on_ready")
    # async def on_ready(self):
    #     print(self.config)

    async def set_icon(self, image_name):
        try:
            guild = await self.bot.fetch_guild(self.config["settings"]["server_id"])
            with open(f"images/{image_name}", 'rb') as f:
                Logger.info("Uploading image...")
                await guild.edit(icon=f.read())
            self.prev_img = image_name
            Logger.info(f"\tSet to: {image_name}")
        except FileNotFoundError:
            Logger.fatal(f"File not found : {image_name} : Can't set image.")

    async def image_loop(self):
        await self.bot.wait_until_ready()

        events = self.config["events"]
        settings = self.config["settings"]
        default_image = settings["default_image_name"]
        
        while True:
            today = datetime.datetime.today()
            t_m = str(today.month) # Today month : str
            t_d = str(today.day) # Today day : str
            
            for event in events:
                event_info = events[event]

                ds_m, ds_d = event_info["date_start"].split("-") # Date start month : str, date start day : str
                de_m, de_d = event_info["date_end"].split("-") # Date end month : str, date end day : str

                if (t_m, t_d) == (ds_m, ds_d): # If today is start
                    event_image = event_info["image_name"]
                    if not self.prev_img == event_image:
                        await self.set_icon(event_image)
                    break
                elif (t_m, t_d) == (de_m, de_d): # If today is end
                    if not self.prev_img == default_image:
                        await self.set_icon(default_image)
                    break
                else: # If neither
                    # Do nothing
                    pass

            # print("Current Date:", datetime.datetime.today())

            await asyncio.sleep(3600) # Every hour, sleep


def setup(bot):
    bot.add_cog(Background(bot))
