#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20761469
API_HASH = "928a78ee6d2f45f9cec4cb2d2d1a5c51"
BOT_TOKEN = "6445303595:AAFXtf42JBC6YK8Z6Rvjge9fZXicLIjnXtM"
SESSION = "BAE8y30AWLC1TWX4OhC5PhEM3SWCjo6tJkgRWv_yIMCUniPUy_41DQc0NRelc-f5OUcLkRMIm_xX-4chI4Gi_VXfFdhwJtNmOhAbZstBqsg4yp3VCEnEx5K6qWlka6AyeZuSH_dFwBPYMFAXYJFHVyvvmp1dhDgEqmNkoft1jnou0c5gPYyKL7EuJzimy9dZfqHKQWTBi4UCpiBH-2GEsTUomMRcOrbqKlzPPOeO1jNn3dVtESTUkknClk5Yy1GTpIziSbpNAMsuYLdUf6glNkr5DtjHjYkgPTeYfl6yw3Y3yOkaUGFDE7hF6vbDUFV7x8L7OcfHkPCTAhsPaTQgTUbB0wDLswAAAAFiFRH5AA"
FORCESUB = "baixarrestritotelegram"
AUTH = 5940515321

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
