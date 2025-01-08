# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Mongo Veritabanınıza bağlanma...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Alexa
    LOGGER(__name__).info("Mongo Veritabanınıza bağlanma.")
except:
    LOGGER(__name__).error("Mongo Veritabanınıza bağlanılamadı.")
    exit()

## Database For Broadcast Subscription By Team Alexa
MONGODB_CLI = AsyncIOMotorClient(MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
