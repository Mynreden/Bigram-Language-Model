import telebot
from telebot import types
from Models.BigramModel import read_data, BigramLanguageModel, create_bigram_model
from Models.TrigramModel import TrigramLanguageModel, create_trigram_model
from Models.NgramModel import NgramLanguageModel, create_ngram_model

with open('token.txt', 'r') as f:
    token = f.read()

bot = telebot.TeleBot('1596944937:AAHDpnFZmLolunh_a11b5THEOrQAFZDbcys')
URL: str = 'datasets/names.txt'

data = read_data(URL)
bigram = create_bigram_model(data)
trigram = create_trigram_model(data)
ngram = create_ngram_model(data, 4)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Bigram Language Model")
    btn2 = types.KeyboardButton("Trigram Language Model")
    btn3 = types.KeyboardButton("N-gram Language Model")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Hello, {0.first_name}! I can generate names using various methods".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Bigram Language Model"):
        bigram_chat(message)

    elif(message.text == "Trigram Language Model"):
        trigram_chat(message)

    elif(message.text == "N-gram Language Model"):
        bot.send_message(message.chat.id, text="Choose N number. Based on last N - 1 numbers language model predict next character")

    elif(message.text.isnumeric()):
        global ngram
        n = int(message.text)
        ngram = create_ngram_model(data, n)
        ngram_chat(message)


def bigram_chat(message):
    bot.send_message(message.chat.id, text="Generated name: {}".format(bigram.generate()))

def trigram_chat(message):
    bot.send_message(message.chat.id, text="Generated name: {}".format(trigram.generate()))

def ngram_chat(message):
    bot.send_message(message.chat.id, text="Generated name: {}".format(ngram.generate()))

bot.polling(none_stop=True)
