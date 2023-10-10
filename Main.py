from aiogram import Bot, Dispatcher, types, executor

# import aiogram

import Token
import You_Money_URL
import klava

bot = Bot(Token.Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=["Pay"])
async def pay(message: types.Message):
    URL, payment = You_Money_URL.creat_Oplata()

    await  message.answer("Вот ссылка на платёж:", reply_markup=klava.oplata(URL, payment))


@dp.callback_query_handler()
async def chek(call: types.CallbackQuery):
    if call.message["text"] == "Вот ссылка на платёж:":
        answer = You_Money_URL.oplata_chek(call.data)
        if answer:
            await  bot.send_message(chat_id=call.from_user.id, text="Оплата прошла без ошибок!")
        else:
            await  bot.send_message(chat_id=call.from_user.id, text="Оплата прошла с ошибкой ошибок!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
