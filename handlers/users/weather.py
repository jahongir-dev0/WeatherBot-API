from aiogram import types
from loader import dp
from data.config import OPENWEATHER_API_KEY, BASE_URL
import requests

def get_weather(city):
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "uz"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            name = data["name"]
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return (f"🌆 Shahar: {name}\n"
                    f"🌡 Harorat: {temp}°C\n"
                    f"🌥 Ob-havo: {description}\n"
                    f"💧 Namlik: {humidity}%\n"
                    f"🌬 Shamol tezligi: {wind_speed} m/s")
        else:
            return f"❌ Xato: {data.get('message', 'Malumot topilmadi.')}"
    except Exception as e:
        return f"❌ Xato: {e}"

@dp.message_handler()
async def send_weather(message: types.Message):
    city = message.text.strip()
    weather_info = get_weather(city)
    await message.answer(weather_info)
