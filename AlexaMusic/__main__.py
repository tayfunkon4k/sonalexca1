# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall, GroupCallNotFound

import config
from config import BANNED_USERS
from AlexaMusic import LOGGER, app, userbot
from AlexaMusic.core.call import Alexa
from AlexaMusic.misc import sudo
from AlexaMusic.plugins import ALL_MODULES
from AlexaMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AlexaMusic").error("Pyrogram dize oturumu ekleyin ve ardından deneyin...")
        sys.exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AlexaMusic.plugins" + all_module)
    LOGGER("AlexaMusic.plugins").info("Gerekli Modüller Başarıyla İçe Aktarıldı.")
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except (NoActiveGroupCall, GroupCallNotFound):
        LOGGER("AlexaMusic").error(
            "[ERROR] - \n\nGrup sesli sohbetini açın ve ertelemeyin, aksi takdirde çalışmayı bırakacağım, teşekkürler."
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("AlexaMusic").info("Sago Müzik Bot Başarıyla Başlatıldı")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AlexaMusic").info("Sago Müzik Bot durduruluyor...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("AlexaMusic").info("Sago Müzik Bot Durduruldu...")
