from aiogram import Bot, Dispatcher, types, executor
import qrcode
# import aiogram

import Token
import You_Money_URL
import klava

bot = Bot(Token.Token)
dp = Dispatcher(bot)

bot = Bot(Token.Token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['Bo'])
async def process_start_command(message: types.Message):
    file_open = open("site.png", 'rb')

    await bot.send_photo(message.from_user.id, file_open)


@dp.message_handler()
async def pay(message: types.Message):
    try:
        money = int(message.text)
        URL, payment = You_Money_URL.creat_Oplata(str(money))

        await  message.answer("Какое действие вы хотите выполнить?", reply_markup=klava.oplata(URL, payment))

        data = klava.oplata(URL, payment)

        filename = "site.png"

        img = qrcode.make(data)

        img.save(filename)
    except:
        await message.answer("Некоректные данные")


@dp.callback_query_handler()
async def chek(call: types.CallbackQuery):
    if call.message["text"] == "Какое действие вы хотите выполнить?":
        answer = You_Money_URL.oplata_chek(call.data)
        if answer:
            await  bot.send_message(chat_id=call.from_user.id, text="Оплата прошла без ошибок!")
        else:
            await  bot.send_message(chat_id=call.from_user.id, text="Оплата прошла с ошибкой!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
