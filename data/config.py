from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()  # .env faylini o'qish

# .env fayl ichidan qiymatlarni o'qish
BOT_TOKEN = env.str("BOT_TOKEN")  # Telegram bot token
ADMINS = env.list("ADMINS")  # Adminlar ro'yxati
IP = env.str("ip")  # IP manzili
OPENWEATHER_API_KEY = env.str("API_KEY")  # OpenWeather API kaliti
BASE_URL = env.str("BASE_URL")  # OpenWeather API URL
