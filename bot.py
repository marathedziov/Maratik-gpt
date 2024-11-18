#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import requests
import telebot
from dotenv import load_dotenv
import os


def gpt(text):
    prompt = {
        "modelUri": "gpt://b1ghnehmnn3n3dvbqi90/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "10000"
        },
        "messages": [
            {
                "role": "assistant",
                "text": text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNz9XUQGq4KhejXKZ-8PLoDVwLZrPGARRazGnK"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']


load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """Привет, это нейро-бот Маратика. Что тебя интересует?""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, gpt(message.text))


bot.infinity_polling()
