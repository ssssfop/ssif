import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Amort Music AR")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ALIVE_NAME = getenv("ALIVE_NAME", "AmortMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "AmortMusicARBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "amortassistantar")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kurd_botschat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "amortmusic")
OWNER_NAME = getenv("OWNER_NAME", "hama_refaat") # isi dengan username kamu tanpa simbol @
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False")) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/")
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
