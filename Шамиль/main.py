from aiogram import Bot, Dispatcher
import qrcode

# import aiogram

import Token
import You_Money_URL
import klava

bot = Bot(Token.Token)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['Bo'])
# async def process_start_command(message: types.Message):

from aiogram import Bot, Dispatcher, executor, types
b = Bot(token=Token.Token)



dp = Dispatcher(bot)

async def send_message(message: types.Message):
    await b.send_message(chat_id = Token.chat_id, text=message)



# TEST


def createFile():
    file_open = open("site.png", 'rb')
    return  file_open

    # await bot.send_photo(message.from_user.id, file_open)


@dp.message_handler()
async def pay(message: types.Message):
    try:
        # await message.answer("knopka", reply_markup=klava.testButton())

        money = int(message.text)

        URL, payment = You_Money_URL.creat_Oplata(str(money))

        await  message.answer("Какое действие вы хотите выполнить?", reply_markup=klava.oplata(URL, payment))

        data = klava.oplata(URL, payment)

        print(data)

        filename = "site.png"

        img = qrcode.make(data)

        img.save(filename)
    except:
        await message.answer("Каким образом клиент будет оплачивать текстовое сообщение!?")


@dp.callback_query_handler()
async def chek(call):
    if call.data == "????":
        print(call.message.values)
        file_open = createFile();
        await bot.send_photo(call.from_user.id, file_open)
    else:
        answer = You_Money_URL.oplata_chek(call.data)
        if answer:
            await bot.send_message(chat_id=call.from_user.id, text="Оплата прошла без ошибок!")
        else:
            await bot.send_message(chat_id=call.from_user.id, text="Оплата прошла с ошибкой!")


if __name__ == "__main__":
    executor.start(dp, send_message("Здравствуйте, для какой суммы вам нужна оплата?"))
    executor.start_polling(dp, skip_updates=True)
