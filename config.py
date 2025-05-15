from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Ambil variabel dari environment
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
