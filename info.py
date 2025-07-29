import re
from os import environ
from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Main
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get("API_ID", "14689508"))
API_HASH = environ.get("API_HASH", "79413cfe2d8cc93ddf1815ef588e80d5")
BOT_TOKEN = environ.get("BOT_TOKEN", "0")
PORT = environ.get("PORT", "8082")

# Owners
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "5672857559").split()
]
OWNER_USERNAME = environ.get(
    "OWNER_USERNAME", "Nobita_X_Surya"
)  # without @ or https://t.me/
USERNAME = environ.get("USERNAME", "@Nobita_X_Surya")  # ADMIN USERNAME

# Database Channel
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "-1002880915492").split()
]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002822419908"))
AUTH_REQ_CHANNEL = int(environ.get("AUTH_REQ_CHANNEL", "-1002819669622"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002616610717"))
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "-1002251993743"))
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "-1002878427403"))

# MongoDB
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")

# Files index database url
FILES_DATABASE = environ.get("FILES_DATABASE", "mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "jisshu")

# Other Channel's
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002710457656"))
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "0"))
request_channel = environ.get("REQUEST_CHANNEL", "--1002817146570)
REQUEST_CHANNEL = (
    int(request_channel)
    if request_channel and id_pattern.search(request_channel)
    else None
)
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "-1002880915492)

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "-1002710457656")
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/Nobita_X_Movie_Chat")

# Verification
IS_VERIFY = is_enabled("IS_VERIFY", False)
# ---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")
VERIFY_IMG = environ.get(
    "VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"
)
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "omegalinks.in")
SHORTENER_API2 = environ.get(
    "SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799"
)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "omegalinks.in")
SHORTENER_API3 = environ.get(
    "SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799"
)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "14400"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "14400"))

# Language & Quality & Season & Year
LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
    "marathi",
]
QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures And Reaction
import re
from os import environ
from Script import script

# This regex is used to check if a string is a valid user/channel ID
# A valid ID starts with an optional '-' and is followed by digits.
id_pattern = re.compile(r"^-?\d+$")


def is_enabled(value, default):
    if value is None:
        return default
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Main
SESSION = environ.get("SESSION", "Media_search")
API_ID = int(environ.get("API_ID", "14689508"))
API_HASH = environ.get("API_HASH", "79413cfe2d8cc93ddf1815ef588e80d5")
BOT_TOKEN = environ.get("BOT_TOKEN", "0") # Replace "0" with your actual bot token in environment variables
PORT = environ.get("PORT", "8082")

# Owners
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "5672857559").split()
]
OWNER_USERNAME = environ.get("OWNER_USERNAME", "Nobita_X_Surya")
USERNAME = environ.get("USERNAME", "@Nobita_X_Surya")

# Database Channel
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "-1002880915492").split()
]

# ForceSub Channel & Log Channels
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002822419908")) if environ.get("AUTH_CHANNEL") else None
AUTH_REQ_CHANNEL = int(environ.get("AUTH_REQ_CHANNEL", "-1002819669622")) if environ.get("AUTH_REQ_CHANNEL") else None
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002616610717")) if environ.get("LOG_CHANNEL") else None
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "-1002251993743")) if environ.get("LOG_API_CHANNEL") else None
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "-1002878427403")) if environ.get("LOG_VR_CHANNEL") else None

# MongoDB
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")

# Files index database url
FILES_DATABASE = environ.get("FILES_DATABASE", "mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "jisshu")

# Other Channel's
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", "-1002710457656")) if environ.get("SUPPORT_GROUP") else None
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "0")) if environ.get("DELETE_CHANNELS") else None
request_channel = environ.get("REQUEST_CHANNEL", "-1002817146570")
REQUEST_CHANNEL = (
    int(request_channel)
    if request_channel and id_pattern.search(request_channel)
    else None
)
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "-1002880915492")) if environ.get("MOVIE_UPDATE_CHANNEL") else None

# Added Link Here Not Id
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "https://t.me/Nobita_X_Surya")
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/Nobita_X_Movie_Chat")

# Verification
IS_VERIFY = is_enabled(environ.get("IS_VERIFY"), False)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "omegalinks.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "omegalinks.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "3097623f852197a9ce40d1212aaa8bbf2803e799")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "omegalinks.in")
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "14400"))
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "14400"))

# Language & Quality & Season & Year
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam", "bengali", "marathi", "gujarati", "punjabi"]
QUALITIES = ["HdRip", "web-dl", "bluray", "hdr", "fhd", "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p", "2K", "2160p", "4k", "5K", "8K"]
YEARS = [f"{i}" for i in range(2025, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]

# Pictures And Reaction
START_IMG = environ.get("START_IMG", "https://envs.sh/Svx.jpg/IMG20250728580.jpg")
FORCESUB_IMG = environ.get("FORCESUB_IMG", "https://envs.sh/Svx.jpg/IMG20250728580.jpg")
REFER_PICS = environ.get("REFER_PICS", "https://envs.sh/Svx.jpg/IMG20250728580.jpg")
PAYPICS = environ.get("PAYPICS", "https://envs.sh/Svx.jpg/IMG20250728580.jpg")
SUBSCRIPTION = environ.get("SUBSCRIPTION", "https://envs.sh/Svx.jpg/IMG20250728580.jpg")
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]

# Other Functions
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "600"))
AUTO_FILTER = is_enabled(environ.get("AUTO_FILTER"), True)
IS_PM_SEARCH = is_enabled(environ.get("IS_PM_SEARCH"), False)
IS_SEND_MOVIE_UPDATE = is_enabled(environ.get("IS_SEND_MOVIE_UPDATE"), False)
MAX_BTN = int(environ.get("MAX_BTN", "8"))
AUTO_DELETE = is_enabled(environ.get("AUTO_DELETE"), True)
DELETE_TIME = int(environ.get("DELETE_TIME", 1200))
IMDB = is_enabled(environ.get("IMDB"), False)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE_TXT)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION"), False)
PROTECT_CONTENT = is_enabled(environ.get("PROTECT_CONTENT"), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK"), True)
LINK_MODE = is_enabled(environ.get("LINK_MODE"), True)
TMDB_API_KEY = environ.get("TMDB_API_KEY", "0") # Replace "0" with your actual TMDB key if you use it

# Online Streaming And Download
STREAM_MODE = is_enabled(environ.get("STREAM_MODE"), False)
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = "DYNO" in environ
URL = environ.get("FQDN", "example.com") # Replace with your app's URL

# Commands
admin_cmds = [
    "/add_premium - Add A User To Premium",
    "/premium_users - View All Premium Users",
    "/remove_premium - Remove A User's Premium Status",
    "/add_redeem - Generate A Redeem Code",
    "/refresh - Refresh Free Trail",
    "/set_muc - Set Movie Update Channel",
    "/pm_search_on - Enable PM Search",
    "/pm_search_off - Disable PM Search",
    "/set_ads - Set Advertisements",
    "/del_ads - Delete Advertisements",
    "/setlist - Set Top Trending List",
    "/clearlist - Clear Top Trending List",
    "/verify_id - Verification Off ID",
    "/index - Index Files",
    "/send - Send Message To A User",
    "/leave - Leave A Group Or Channel",
    "/ban - Ban A User",
    "/unban - Unban A User",
    "/broadcast - Broadcast Message",
    "/grp_broadcast - Broadcast Messages To Groups",
    "/delreq - Delete Join Request",
    "/channel - List Of Database Channels",
    "/del_file - Delete A Specific File",
    "/delete - Delete A File(By Reply)",
    "/deletefiles - Delete Multiple Files",
    "/deleteall - Delete All Files",
]

cmds = [
    {"start": "Start The Bot"},
    {"most": "Get Most Searches Button List"},
    {"trend": "Get Top Trending Button List"},
    {"mostlist": "Show Most Searches List"},
    {"trendlist": "Get Top Trending Button List"},
    {"plan": "Check Available Premium Membership Plans"},
    {"myplan": "Check Your Current Plan"},
    {"refer": "To Refer Your Friend And Get Premium"},
    {"stats": "Check My Database"},
    {"id": "Get Telegram Id"},
    {"font": "To Generate Cool Fonts"},
    {"details": "Check Group Details"},
    {"settings": "Change Bot Setting"},
    {"grp_cmds": "Check Group Commands"},
    {"admin_cmds": "Bot Admin Commands"},
]
