import discord
import json
from discord.ext.commands import Bot
from discord.ext import commands
from time import sleep
from vkpars import check_requests

import asyncio

Bot = commands.Bot(command_prefix="!")

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def news(ctx):
    channel = Bot.get_channel(701899032678891683)
    count = 9999999
    while count > 0:
        check_requests(5)
        with open("data_file.json", "r", encoding='utf-8') as f:
            text = json.load(f)
            #emb = discord.Embed('Рифмы и панчи')
            emb = discord.Embed(title="К сообществу", url = ('https://vk.com/club33674733'), color=0x39d0d6)
            emb.set_thumbnail(url="https://sun1-14.userapi.com/impg/iYSgEzSqU2d9loZgITJy8yvA8zZ_YGPupp796w/sf1K-uXE8Rc.jpg?size=1280x1280&quality=96&sign=41ceb53e62e0cc6416d32d24857f77ed&type=album")
            emb.add_field(name='Рифмы и Панчи:', value=text, inline=False)
            with open("data_url.json", "r", encoding='utf-8') as fe:
                zz = json.load(fe)
            emb.set_image(url=zz)
            await channel.send(embed=emb)
            await asyncio.sleep(3600)
            count = count - 1

Bot.remove_command('help')

Bot.run('')