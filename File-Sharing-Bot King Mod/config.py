import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

# Bot token from @BotFather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7501427359:AAHINljPljLxX2hkj_QsnbC33-XQtZDJuBw")

# API credentials from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6953769"))
API_HASH = os.environ.get("API_HASH", "44d943e23486a579d46ce7dc7cd19c88")

# Your database channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002034209239"))

# Owner ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2145086581"))

# Port for web server
PORT = os.environ.get("PORT", "8080")

# Database settings
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hariharan011205:DCPmNk8OxjyeI0fe@cluster0.2igcqay.mongodb.net/?retryWrites=true&w=majority")
#Like this:  mongodb+srv://username:password@cluster8.7kxb6.mongodb.net/?retryWrites=true&w=majority

#Probably Bot Username
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

# Force subscription channels (support for multiple channels)
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002815649969"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002695961193"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002162213617"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002673809386"))

#Don't Touch This 😡
LINKSHORTX_API=os.environ.get("LINKSHORTX_API",'d86f57a6ae444bdc63318e7b111a02b8edb8a59a')

# Workers for the bot
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message and image
START_PIC = os.environ.get("START_PIC", "https://img.freepik.com/free-photo/medium-shot-anime-style-man-portrait_23-2151067508.jpg?t=st=1733125602~exp=1733129202~hmac=d6cde9786405087258d9b0968ab5dcfdc64e14d16b24db5b9996f0f2d5e7ab81&w=826")
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {first}\n\nI can store private files in a specified channel, and other users can access them via a special link."
)

# Admins list
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "1103392937 ").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.append(OWNER_ID)  
ADMINS.append(746480452)  

# Force subscription message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "Hello {first} {last}\n\n<b>You need to join my Channel/Group to use me.\n\nKindly join the channels listed below:</b>"
)

# Custom caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", '{previouscaption}\n <code>{filename}</code> <blockquote><b>Bʏ @Pocket_FmEnglish</b></blockquote>')

# File protection
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set to `False` to disable auto link creation, or `True` to enable Auto link creation.
ENABLE_LINK_CREATION = False  

# Fetch the AUTO_DELETE_TIME from environment variable (default to 0 if not set)
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))

# Convert AUTO_DELETE_TIME to a human-readable format
def format_time(seconds):
    if seconds < 60:
        return f"{seconds} second{'s' if seconds != 1 else ''}"
    elif seconds < 3600:
        minutes = seconds // 60
        return f"{minutes} minute{'s' if minutes != 1 else ''}"
    elif seconds < 86400:
        hours = seconds // 3600
        return f"{hours} hour{'s' if hours != 1 else ''}"
    else:
        days = seconds // 86400
        return f"{days} day{'s' if days != 1 else ''}"

# Dynamic message for AUTO_DELETE_TIME
deletetime = format_time(AUTO_DELETE_TIME)

AUTO_DELETE_MSG = os.environ.get(
    "AUTO_DELETE_MSG",
    f"<b>This file will be automatically deleted in {deletetime}.</b>\n <blockquote><b>Please ensure you have listened to all the above episodes before generating more episodes.</b></blockquote>"
)

AUTO_DEL_SUCCESS_MSG = os.environ.get(
    "AUTO_DEL_SUCCESS_MSG",
    "<b>Your file has been successfully deleted. Thank you for using our service. ✅</b>"
)

# Output the messages
print(AUTO_DELETE_MSG)
print(AUTO_DEL_SUCCESS_MSG)


# Disable share button in channels
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ You Are not my Owner Get OUT! 😡"

# Logging configuration
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
