from pathlib import Path

import telebot
from telebot import types
import yaml
import logging

from constants import HELLO

LOGGER = logging.getLogger()

bot_config_path = Path('src/config.yaml')
with open(bot_config_path, 'r') as iof:
    bot_config = yaml.load(iof, Loader=yaml.Loader)

bot = telebot.TeleBot(bot_config['token'])

@bot.message_handler(commands=['start'])
def start(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    if last_name is None:
        name = first_name
    else:
        name = f"{first_name} {last_name}"
    mess = f"Привет, <b>{name}</b>"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['game'])
def get_games(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Играть в игры', callback_game='test'))
    bot.send_message(message.chat.id, 'Угадайка слов', reply_markup=markup)


@bot.message_handler(commands=['help'])
def get_games(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Сыылка на гугл')
    start = types.KeyboardButton('Start')
    games = types.KeyboardButton('Games')
    markup.add(website, start, games)
    bot.send_message(message.chat.id, 'Yat yat yat', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'yatyat':
        bot.send_message(message.chat.id, message, parse_mode='html')
    elif message.text in HELLO:
        bot.send_message(message.chat.id, 'И тебе привет', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать', parse_mode='html')





bot.polling(none_stop=True)

