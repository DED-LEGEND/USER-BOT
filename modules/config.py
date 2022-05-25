import re
import os
import aiohttp
import asyncio
import logging
import requests
from os import getenv
from pyrogram.types import *
from datetime import datetime
from dotenv import load_dotenv
from pyrogram import Client, filters, idle
from apscheduler.schedulers.asyncio import AsyncIOScheduler

if os.path.exists("local.env"):
    load_dotenv("local.env")
    
que = {}
admins = {}
CMD_HELP = {}
START_TIME = datetime.now()
scheduler = AsyncIOScheduler()
aiohttpsession = aiohttp.ClientSession()
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_HASH = getenv("API_HASH", "32aa547bd6cc2e9f61063cd31e0bc0a5")
API_ID = int(getenv("API_ID", "10655360"))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/72b5352f934e8caa6dcf1.jpg")
DATABASE_URL = getenv("DATABASE_URL", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://pyrobot:pyrobot@cluster0.lsr4q.mongodb.net/?retryWrites=true&w=majority")
STRING_SESSION = getenv("STRING_SESSION", "BQC6dCYaSzYN8hrtu6Qhh789oJak-z3SALKKiQpsEy-aE__rd8NIH_-hxG1dvmxuFx4PDOUb_7ivYsMPXQFwWGqE_W_mpmwJZ5e_jJZ-uqqyszKTT1g7fz2sGx-0oCOsLxoAwcPniUJsA2WAs9ncdwCmQ3KCkTqDkfbV_mjc8CN9tlfL39r9v_PAQUqGx7KJ0XY8ZiI01u0cqq7uqogwkgKhUuqGji01ym0Ptg9FfJE5SpRxKKBudIv-N0qD06_LXGCpiYA-GeYkFozvV3Z7YtTOrLRhtO_2yuD9B_VbWi_jPl_fEwrl_AnCw1HwNQgAXloNk1KrI3VYIeXvX82hk-9nVNiTrAA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split()))
LOGS_GROUP_ID = getenv("LOGS_GROUP_ID", "-1001717936747")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "*").split())

if LOGS_GROUP_ID:
    Owner = LOGS_GROUP_ID
else:
    Owner = 777000
