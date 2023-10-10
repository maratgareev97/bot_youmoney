from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def oplata(url, id):
    klava = InlineKeyboardMarkup()
    klava.add(InlineKeyboardButton("ССылка:", url = url))
    klava.add(InlineKeyboardButton("Проверить оплату", callback_data = id))
    return klava
