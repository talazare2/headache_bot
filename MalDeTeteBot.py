import telebot
import requests
import json
import logging
from dialogs_tgbot import dialog_message
from translate_module import translate_mes, translate_mes_API
from analysis import hea_df
from googletrans import Translator
import pandas as pd

src_gl = 'en'
dest_gl = 'ru'
data_collected = []
all_mes = dialog_message(dest_gl)
translator = Translator()
api_token = '6731806282:AAHhovoqO3dg6Auza8Ov5OxIRLLr5LFLhvA'
bot = telebot.TeleBot(api_token)
@bot.message_handler(content_types=['text'])


def start(message):
    if message.text == 'start':
        lang_mes_en = 'Hello! Please, choose your language!'
        lang_mes_ru = translator.translate(lang_mes_en, src='en', dest='ru').text
        lang_mes_fr = translator.translate(lang_mes_en, src='en', dest='fr').text
        lang_mes = f'{lang_mes_en}\n{lang_mes_ru}\n{lang_mes_fr}'
        options_en = 'Supported languages'
        options_ru = translator.translate(options_en, src='en', dest='ru').text
        options_fr = translator.translate(options_en, src='en', dest='fr').text
        options_lang = f'{options_en}: en, ru, fr\n{options_ru}: en, ru, fr\n{options_fr}: en, ru, fr'
        bot.send_message(message.from_user.id, lang_mes)
        bot.send_message(message.from_user.id, options_lang)
        bot.register_next_step_handler(message, set_lang)
    else:
        unind_mes_en = 'To launch the bot type \"start\"'
        unind_mes_ru = 'Чтобы запустить бот введите \"start\"'
        unind_mes_fr = 'Pour lancer le bot entrez \"start\"'
        unind_mes = f'{unind_mes_en}\n{unind_mes_ru}\n{unind_mes_fr}'
        bot.send_message(message.from_user.id, unind_mes)


def set_lang(message):
    global src_gl
    global dest_gl
    src_gl = 'en'
    hea_df['lang'] = message.text
    if message.text == 'en':
        dest_gl = 'en'
        bot.send_message(message.from_user.id, 'Selected language: English')
        headache_level(message)
    elif message.text == 'ru':
        dest_gl = 'ru'
        bot.send_message(message.from_user.id, 'Выбран русский язык')
        headache_level(message)
    elif message.text == 'fr':
        dest_gl = 'fr'
        bot.send_message(message.from_user.id, 'Vous avez sélectionné Français')
        headache_level(message)
    else: 
        unind_mes_en = 'Language is not supported! Type en for English, ru for Russian or fr for French.'
        unind_mes_ru = 'Язык не поддерживается! Введите en для английского языка, ru для русского языка и fr для французского языка.'
        unind_mes_fr = 'Le langue non supportée! Entrez en pour Anglais, ru pour Russe et fr pour Français.'
        unind_mes = f'{unind_mes_en}\n{unind_mes_ru}\n{unind_mes_fr}'
        bot.send_message(message.from_user.id, unind_mes)

def headache_level(message):
    mes_intro = all_mes[0]
    mes_halevel = all_mes[1]
    bot.send_message(message.from_user.id, mes_intro)
    bot.send_message(message.from_user.id, mes_halevel)
    bot.register_next_step_handler(message, localisation)

def localisation(message):
    data_collected.append(message)
    img = open('headache.png', 'rb')
    mes_haloc = all_mes[2]
    bot.send_photo(message.from_user.id, img)
    bot.send_message(message.from_user.id, mes_haloc)
    bot.register_next_step_handler(message, localisation)

if __name__ == '__main__':
    bot.polling(none_stop=True)