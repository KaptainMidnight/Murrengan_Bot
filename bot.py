#!/usr/bin/venv python
# -*- coding: utf-8 -*-


from telebot import TeleBot

token = "851940626:AAEh8TpdiGqjFtQy-aRgm36nA-HvG1A1CN4"

bot = TeleBot(token)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.send_message(message.chat.id, text=
    f'Добро пожаловать, @{message.from_user.username}!\n\n'
    f'[ Trello ](https://trello.com/b/yfjytAFU/murrengan),\n'
    f'[ Стримы Twitch ](https://www.twitch.tv/murren_egor),\n'
    f'[ Мой канал на Youtube ](https://www.youtube.com/murrengan),\n'
    f'[ Мой Vk ](https://vk.com/egor.a.komarov)\n\n'
    'Да прибудет с тобой сила!\n'
    'Murrengan')


if __name__ == '__main__':
    bot.polling(none_stop=True)
