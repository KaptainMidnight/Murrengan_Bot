#!/usr/bin/venv python
# -*- coding: utf-8 -*-


from telebot import TeleBot, types

token = "<token>"

bot = TeleBot(token)


# @bot.message_handler(content_types=['text'])
# def send(message):
#     mat = ['блять', 'черт', 'пошел нахуй']
#     response = message.text
#     for i in mat:
#         print(i)
#         print(i if response in i else "Список не содержит заданного элемента")


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    markup = types.InlineKeyboardMarkup()
    btn_github = types.InlineKeyboardButton(text='Github', url='https://github.com/Murrengan/murr')
    btn_trello = types.InlineKeyboardButton(text='Trello', url='https://trello.com/b/yfjytAFU/murrengan')
    markup.add(btn_github, btn_trello)
    bot.send_message(message.chat.id, text=
    f'@{message.from_user.username}, привет!\n'
    'Добро пожаловать в группу.\n'
    'Ниже основные штуки по проекту.\n'
    'И да пребудет с тобой сила!', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
