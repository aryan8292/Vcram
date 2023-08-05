import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "21966647"))
API_HASH = getenv("API_HASH", "cf9724197b0d6e7d8a53e46763b34fd1")

BOT_TOKEN = getenv("BOT_TOKEN", "6189174968:AAFgUKQBOvo5b-C7rjALo38qqXnlGdu3a20")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sakilanowar78:atIAQ0iJ2bwlMig7@cluster0.1mqytch.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001923845903"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "ᴀʏᴇsʜᴀ ダ ᴍᴜsɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "5079629749").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/ARY_botZ")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ArchBots")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ARCH_SUPPORTS")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "1200"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "cedb7e72e71a4ffb924507be68de51ca")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c053dde8eafa44caa05269363088820c")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQCjfkb7pMe55tiQzx_sa46MuK4iw9t0bzPfInJaH7TWN9PnEf6yasPaIEz8N9VCZFhGkUbvUBcFZGb7LIvz6C8wmO0bkiqbe8coyR8huuLoJUDOKtEfn6wqGKuU-ELYnV832dDlitzYIfi0b-IN37pbPc1vktjoBuvOyvDzTiRFD-42c6VDhogwKcmpOIJj2YQYu4KWNQmH5FGsPjvplDIj5K8_fzIzc1qJm5jtUKMSOakI-S_BW7PClF0iUzfQWBv_VPzzYn3lHKkqvfO1RUXqFpi3eJbk5qPOn3CJQYQFafd7ZgwYa4YfIwbsjoL9UeV3Dg6bwrUus1tzZD_vwkIiAAAAAUxuCvAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/18d800f7d1780150f014d.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/32170ca71c9e08a1f9d29.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/ef68d2b338898282ab929.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/24b33336ad6707eea4e36.jpg"

STATS_IMG_URL = "https://telegra.ph/file/7905a1b346d2f94ced3ac.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/8a8df328bcd8787d00aea.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/34f0d59f33ea16503e07b.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/a174be54c70f1fd5f10e1.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1096a1a7748f2e484884c.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/04f6450c6386e1908254c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/67a78ee4b3979c8d389f2.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/1267b1baec10d7f3722f6.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/06afcbbd20953e374e663.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/32170ca71c9e08a1f9d29.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/18d800f7d1780150f014d.jpg"
