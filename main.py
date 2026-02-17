import telebot

token ="8257557195:AAE-7Rf8XgiQdfCZRicQxYNRZimQzw_dpR0"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я экологичный Telegram бот. Что вы хотите?")
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! У вас есть вопрос?")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Возращайся")
@bot.message_handler(commands=['ecology'])
def send_bye(message):
    bot.reply_to(message, "Спасибо природе")

razloenie = f"""
Некоторые вещи и сколько разлагаются:
Полиэтилен (ПЭ) — от 100 до 1000 лет.
Полиэтилентерефталат (ПЭТ) — около 200 лет.
Полипропилен (ПП) — от 20 до 30 лет.
Поливинилхлорид (ПВХ) — от 100 до 400 лет.
Бумага	—  2-6 недель.
Картон	— 2-3 месяца.
Пищевые отходы — от 2 дней до 6 месяцев.
Стекло	— 1000+ лет (до 1 млн лет). 
"""

@bot.message_handler(commands=['razloenie'])
def send_bye(message):
    bot.reply_to(message, razloenie)

@bot.message_handler(commands=['battery'])
def send_bye(message):
    bot.reply_to(message, "Батарея - уже не сильно распространённая вещь, но очень опасная. Надо сдавать пустые батарейки в специализированные пункты приёма. ")

@bot.message_handler(commands=['plastic'])
def send_bye(message):
    bot.reply_to(message, "Пластик - самый распространённый нефтепродукт. Он может разлагаться до 1000 лет! Лучше всего сдавать на переработку.")

@bot.message_handler(commands=['help'])
def send_bye(message):
    bot.reply_to(message, "Команды: /help, /start, /hello, /bye, /battery, /plastic, /razloenie")
bot.polling()