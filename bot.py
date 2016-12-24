import telebot
import config
import sqlite3
#import db
import selectionsDataBase


# Настраиваем соединение с нашим ботом
bot = telebot.TeleBot(config.token)


def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я информационная система расписания 315 группы")


# query = "SELECT  * FROM pn_chet"
# result = selectionsDataBase.query(query)
# print(result)

#Бот отвечает на команды
@bot.message_handler(commands=['start'])
def handle_text(message):
	user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
	user_markup.row("Четная")
	user_markup.row("Нечетная")
	bot.send_message(message.from_user.id, 'Выберите неделю:', reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_text(message):
	bot.send_message(message.from_user.id, 'Расписание само подскажет, что нужно выбрать. Неделя:четная и нечетная. День: Пн, Вт, Ср, Чт, Пт, Сб ')

#при выборе четной недели предлагается выбрать вариант дня недели с помощью кнопок
@bot.message_handler(func=lambda mess: "Четная" == mess.text, content_types=['text'])
def choose_day(message):
    day_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    day_markup.row("Пн", "Вт", "Ср")
    day_markup.row("Чт", "Пт", "Сб")
    bot.send_message(message.from_user.id, 'Выберите день недели:', reply_markup=day_markup)
    print(message)
#после выбора дня недели высылается расписание на выбранный день
@bot.message_handler(func=lambda mess: "Пн" == mess.text or \
                         "Вт" == mess.text or \
                         "Ср" == mess.text or \
                         "Чт" == mess.text or \
                         "Пт" == mess.text or \
                         "Сб" == mess.text, content_types=['text'])
def show_day(message):
    if message.text == "Пн":
        bot.send_message(message.from_user.id, "Понедельник:")
        query = "SELECT  * FROM pn_chet"  # запрос из бд для понедельника
        result = selectionsDataBase.query(query)
        bot.reply_to(message, str(result))
    elif message.text == "Вт":
        bot.send_message(message.from_user.id, "Вторник:")
        query = "SELECT  * FROM vt_chet"  # запрос из бд для вторника
        result = selectionsDataBase.query(query)
        print(result)
        bot.reply_to(message, str(result))
    elif message.text == "Ср":
        bot.send_message(message.from_user.id, "День для самостоятельной работы")
    elif message.text == "Чт":
        bot.send_message(message.from_user.id, "Четверг:")
        query = "SELECT  * FROM cht_chet"  # запрос из бд для четверга
        result = selectionsDataBase.query(query)
        print(result)
        bot.reply_to(message, str(result))
    elif message.text == "Пт":
        bot.send_message(message.from_user.id, "Пятница:")
        query = "SELECT  * FROM pt_chet"  # запрос из бд для пятницы
        result = selectionsDataBase.query(query)
        print(result)
        bot.reply_to(message, str(result))
    elif message.text == "Сб":
        bot.send_message(message.from_user.id, "Суббота:")
        query = "SELECT  * FROM sb_chet"  # запрос из бд для субботы
        result = selectionsDataBase.query(query)
        print(result)
        bot.reply_to(message, str(result))
        # bot.send_message(message.from_user.id, 'Понедельник:', slovar.week_1["Пн"])
        # print(slovar.week_1["Пн"])
        # bot.send_message(message.from_user.id, slovar.week_1)


@bot.message_handler(func=lambda mess: "Нечетная" == mess.text, content_types=['text'])
def choose_day(message):
    day_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    day_markup.row("Пн", "Вт", "Ср")
    day_markup.row("Чт", "Пт", "Сб")
    bot.send_message(message.from_user.id, 'Выберите день недели:', reply_markup=day_markup)

    @bot.message_handler(func=lambda mess: "Пн" == mess.text or \
                                           "Вт" == mess.text or \
                                           "Ср" == mess.text or \
                                           "Чт" == mess.text or \
                                           "Пт" == mess.text or \
                                           "Сб" == mess.text, content_types=['text'])

    def show_day1(message):
        if message.text == "Пн":
            bot.send_message(message.from_user.id, "Понедельник:")
            query = "SELECT  * FROM pn_nechet"  # запрос из бд для понедельника
            result = selectionsDataBase.query(query)
            bot.reply_to(message, str(result))
        elif message.text == "Вт":
            bot.send_message(message.from_user.id, "Вторник:")
            query = "SELECT  * FROM vt_chet"  # запрос из бд для вторника
            result = selectionsDataBase.query(query)
            print(result)
            bot.reply_to(message, str(result))
        elif message.text == "Ср":
            bot.send_message(message.from_user.id, "День для самостоятельной работы")
        elif message.text == "Чт":
            bot.send_message(message.from_user.id, "Четверг:")
            query = "SELECT  * FROM vt_chet"  # запрос из бд для четверга
            result = selectionsDataBase.query(query)
            print(result)
            bot.reply_to(message, str(result))
        elif message.text == "Пт":
            bot.send_message(message.from_user.id, "Пятница:")
            query = "SELECT  * FROM vt_chet"  # запрос из бд для пятницы
            result = selectionsDataBase.query(query)
            print(result)
            bot.reply_to(message, str(result))
        elif message.text == "Сб":
            bot.send_message(message.from_user.id, "Суббота:")
            query = "SELECT  * FROM vt_chet"  # запрос из бд для субботы
            result = selectionsDataBase.query(query)
            print(result)
            bot.reply_to(message, str(result))


# @bot.message_handler(commands=['help'])
# def send_welcome(message):
#     bot.reply_to(message, )

# Бот отвечает на все сообщения по умолчанию
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

# Запуск бота
bot.polling()


