import telebot
from bot_logic import gen_pass

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=["pass"])
def send_pass(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Вот твой пароль: {password}")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я могу выполнить следующие команды: \n /start - Начать работу\n /help - Показать это сообщение\n /hello - Поприветствовать пользователя\n /bye - Попрощаться с пользователем\n /pass - Сгенерировать пароль")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
