from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def oplata(url, id):
    klava = InlineKeyboardMarkup()
    klava.add(InlineKeyboardButton("ССылка:", url=url))
    klava.add(InlineKeyboardButton("Отправить QR", callback_data="????"))
    klava.add(InlineKeyboardButton("Проверить оплату", callback_data=id))

    return klava


# def testButton():
#     kl = InlineKeyboardMarkup()
#     kl.add(InlineKeyboardButton("Отправить QR", callback_data="????"))
#     # print(kl)
#
#     return kl
