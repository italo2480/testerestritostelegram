#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("7534644", default=None, cast=int)
API_HASH = config("aada368b82de5c6c3534677bdb98a75b", default=None)
BOT_TOKEN = config("aada368b82de5c6c3534677bdb98a75b", default=None)
SESSION = config("AQBy-DQAhynEhgb1fwV-bcLEfpFgnjWMrAQ_YBEhNNDQOuGMT8OnhFmIKUr5DZXW9QbtBUTwvjM2lqEtiGTGMFc_aSTj5oKu2n8RhaieBJkdrdT6kTtf7GBY9_1SC3eCDQPfvluQB_xIXERTiE2c4Zwc6runwfD4uVl5OqXI1kgytQD41gRUetWuSQwCh2ty5Mlm-ZLRFc85MYaFAkcpeszJg83uuCZIMRiUKVl27O8gf9cLmNHd6t-vN-DO7f8jVd20h2CPK8zLcSvBB2UANuMp1t-50c348pLrn0xNOPy2oE3oNyI887fSajln7p-uvJJ_y2wGjDcKpBsp0uLW0wJ2GpNjxgAAAAAYOzNNAA", default=None)
FORCESUB = config("baixarrestritotelegram", default=None)
AUTH = config("406532941", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
