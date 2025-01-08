# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import sys

from pyrogram import Client
import config
from ..logging import LOGGER
from pyrogram.enums import ChatMemberStatus


class AlexaBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            sleep_threshold=180,
            max_concurrent_transmissions=4,
            workers=50,
        )
        LOGGER(__name__).info(f"Bot Başlatıldı...")

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.mention = get_me.mention
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "» Müzik botu başlatıldı, asistan bekleniyor..."
            )
        except:
            LOGGER(__name__).error(
                "Bot, günlük grubuna erişemedi. Botunuzu günlük kanalınıza eklediğinizden ve yönetici olarak tanıttığınızdan emin olun.!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Lütfen Bot'u Grubunuzda Yönetici olarak tanıtın")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"Sago Müzik Bot Başlatıldı. {self.name}")
