# crushe
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27134561"))
API_HASH = getenv("API_HASH", "fa3c15f5ed4e3226ce9a929e4b9b2806")
BOT_TOKEN = getenv("BOT_TOKEN", "") # Make sure this token is valid and the bot is active
OWNER_ID = list(map(int, getenv("OWNER_ID", "922270982").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002293309406") # Make sure this group exists and the bot is an admin
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002433933366"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000000000"))

#AutoDeleteTime
SECONDS = int(getenv("SECONDS", "300")) #5_minutes
