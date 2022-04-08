from decouple import config
import pylast

# discord
TOKEN = config('BOT_TOKEN')

# last.fm api
API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')