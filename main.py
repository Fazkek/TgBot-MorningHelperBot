import requests
import time
import asyncio
import datetime
import threading
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from datetime import date
from bs4 import BeautifulSoup
import re

token = "5787139770:AAG6WQN12KsIKLYCah2iDXTJjobSeiw7aiI"


def timew():
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    s_time = current_time.split(":")
    a = int(s_time[0])
    b = int(s_time[1])
    aft = 24*60-(60*a + b)
    return aft


def sec():
    current_date_time = datetime.datetime.now()
    current_time = str(current_date_time.time())
    s_time = current_time.split(":")
    c = s_time[2].split('.')
    c = int(c[0])

    return c


def weather():
    city = 'Izhevsk'
    open_weather_token = "962f37ebfd48246dca4d838a7b8b6393"

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
    )
    data = r.json()

    weather_description = data["weather"][0]["main"]
    if weather_description in code_to_smile:
        wd = str(code_to_smile[weather_description])
    else:
        wd = "Посмотри в окно, не пойму что там за погода!"

    wla = str(data["main"]["humidity"])
    wind = str(data["wind"]["speed"])
    temp = str(data["main"]["temp"]).split('.')
    temp = temp[0]
    real_temp = str(data["main"]["feels_like"]).split('.')
    real_temp = str(real_temp[0])

    weather_info = '✋Погода в Ижевске: ' + '\n' + '🌡' + temp + '°C' + f' ({real_temp}°C), ' + wd + '\n' + '💦Влажность - ' + wla + '%\n' + f'🌬Ветер - {wind} м/с' + '\n' + f"❗️Данные на: {datetime.datetime.now().strftime('%d.%m %H:%M')}\n"
    return weather_info




def clothes():
    city = 'Izhevsk'
    open_weather_token = "962f37ebfd48246dca4d838a7b8b6393"

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
    )
    data = r.json()



    wind_fix = int(data["wind"]["speed"])
    real_temp = str(data["main"]["feels_like"]).split('.')
    real_temp = int(real_temp[0])

    if 6 <= real_temp <= 10:
        if wind_fix >= 5:

            a = "Сегодня тепло и ветренно"
            b = "Я советую надеть вам ветровку и головной убор"

            return a, b
        else:

            a = "Сегодня тепло"
            b = "Я советую надеть ветровку"

            return a, b
    if 0 <= real_temp <= 5:
        if wind_fix >= 5:

            a = "Сегодня не очень холодно и ветренно"
            b = "Я советую надеть вам шапку, капюшон и шарф"

            return a, b
        else:

            a = "Сегодня не очень холодно"
            b = "Я советую надеть вам шапку"

            return a, b
    if -5 <= real_temp <= -1:
        if wind_fix >= 5:

            a = "Сегодня не очень холодно и ветренно"
            b = "Я советую надеть вам шапку, капюшон и шарф"

            return a, b
        else:

            a = "Сегодня не очень холодно"
            b = "Я советую надеть вам шапку"

            return a, b
    if -10 <= real_temp <= -6:
        if wind_fix >= 5:

            a = "Сегодня прохладно и ветренно"
            b = "Я советую надеть вам тёплую шапку, шарф, капюшон и перчатки"

            return a, b
        else:

            a = "Сегодня прохладно"
            b = "Я советую надеть вам тёплую шапку и перчатки"

            return a, b
    if -15 <= real_temp <= -11:
        if wind_fix >= 5:

            a = "Сегодня холодно и ветренно"
            b = "Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, капюшон и куртку до колена"

            return a, b
        else:

            a = "Сегодня холодно"
            b = "Я советую вам надеть подштанники, тёплую шапку, перчатки и куртку до колена"
            return a, b

    if -20 <= real_temp <= -16:
        if wind_fix >= 5:
            print("Сегодня правда холодно и ветренно")
            print("Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, кофту, капюшон и куртку до колена")

            a = "Сегодня правда холодно и ветренно"
            b = "Я советую вам надеть подштанники, тёплую шапку, шарф, перчатки, кофту, капюшон и куртку до колена"

            return a, b
        else:

            a = "Сегодня правда холодно"
            b = "Я советую вам надеть подштанники, тёплую шапку, перчатки, кофту и куртку до колена"

            return a, b
    if -25 <= real_temp <= -21:
        if wind_fix >= 5:

            a = "Сегодня очень холодно и ветренно"
            b = "Я советую вам не выходить из дома"

            return a, b
        else:

            a = "Сегодня очень холодно"
            b = "Я советую вам надеть надеть подштанники, тёплую шапку, перчатки, кофту и куртку до колена"

            return a, b


def money():
    pog = "https://www.banki.ru/products/currency/cash/usd/izhevsk/"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for usd in soup.find_all('td', class_="currency-table__rate currency-table__darken-bg"):
        usd = usd.find('div', class_="currency-table__large-text")
        usd = usd.text
        usd = f"{usd} ₽"
        return usd


def money_euro():
    pog = "https://www.banki.ru/products/currency/eur/"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for euro in soup.find_all('td', class_="currency-table__rate currency-table__darken-bg"):
        euro = euro.find('div', class_="currency-table__large-text")
        euro = euro.text
        euro = f"{euro} ₽"
        return euro


def btc():
    pog = "https://mainfin.ru/crypto/bitcoin"

    req = requests.get(pog)
    soup = BeautifulSoup(req.text, 'html.parser')

    for btc in soup.find_all('div', class_="crypto_curr_val"):
        btc = btc.text

        return btc


def info():
    euro_ = money_euro()
    weather_ = weather()
    clothes_ = clothes()
    btc_ = btc()
    usd_ = money()
    text = f"{weather_} \n ******************************** \n ❄️{clothes_[0]}❄️ \n ❗️{clothes_[1]}❗️\n ******************************** \n 💰Биткоин: {btc_} \n 💵Доллар: {usd_} \n 💶Евро: {euro_}"
    return text


bot = Bot(token=token)
dp = Dispatcher(bot)


def main_bot(dp):
    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message, markup=None):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton(text="Информация")
        keyboard.add(button_1)
        await message.answer(f"✋Привет! Моя главная задача, заключается в облегчении твоих утренних дел. Я буду отправлять тебе сводку погоды, одежды, которую тебе надо надеть, и курсы валют. Чтобы получить сообщение утром и настроить время, следуй моим инструкциям: \n\n ❗️Чтобы сообщение отправлялось в нужное время - просто отправьте мне его, в подобном формате 7:00\n\n ❗️Если найдёшь какие то недочёты или бот не работает пиши сюда -> @fazk4ek", reply_markup=keyboard)

    @dp.message_handler(content_types=['text'])
    async def main(message: types.Message):

        if message.text == 'Информация':
            a = info()
            a_s = a.split('********************************')
            await bot.send_message(message.chat.id,
                             text=a_s[0])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                             text=a_s[1])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                             text=a_s[2])
            time.sleep(0.8)
            await bot.send_message(message.chat.id,
                             text="Желаю вам продуктивного дня)")

        elif message.text == "Настройка времени":
            time.sleep(0.3)
            await bot.send_message(message.chat.id,
                             text="Отправьте время в таком формате - 7:00")
            time.sleep(0.3)
            await bot.send_message(message.chat.id,
                             text="Если хотите поменять время - просто отправьте мне его")

        elif (re.match(r'([12]\d[:][0-5]\d)|([1-9][:][0-5]\d)', message.text)) is None:
            await bot.send_message(message.chat.id,
                                   text="Нет такой команды!")
        else:
            a = timew()
            c = sec()
            time.sleep(0.3)

            n_time = message.text
            n_time = n_time.split(':')
            z = int(n_time[0])
            v = int(n_time[1])
            x = a + (z*60+v)
            if x > 1440:
                x = x - 1440
            await bot.send_message(message.chat.id, text="Таймер установлен!")
            await asyncio.sleep(x*60-c-2)
            a = info()
            a_s = a.split('********************************')
            await bot.send_message(message.chat.id,
                                   text="Время истекло!")
            time.sleep(1)
            await bot.send_message(message.chat.id,
                                   text=a_s[0])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text=a_s[1])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text=a_s[2])
            time.sleep(0.4)
            await bot.send_message(message.chat.id,
                                   text="Желаю вам продуктивного дня)")


if __name__ == '__main__':
    th2 = threading.Thread(target=main_bot, args=(dp,), daemon=True)
    th2.start()
    executor.start_polling(dp, skip_updates=True)