from decouple import config
import pylast

# discord
TOKEN = config('BOT_TOKEN')

# last.fm api
API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

# last.fm acc
LAST_USER = config("LAST_USER")
LAST_PASS = pylast.md5(config("LAST_PASS"))