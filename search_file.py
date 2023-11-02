import os
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
bot = Bot("6921068092:AAHL6dzfyrgIjQBaQs5-CWi2s6e1CUo6kLI")
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def cmd_test1(message: types.Message):
    await message.reply("Добро пожаловать в бота")
    chatId = message.chat.id
    def searchFile(chatId):
        dir = "file_token"
        os.chdir(dir)
        dir = os.getcwd()
        if os.path.exists(str(chatId)):
            f = open(str(chatId))
            fileRead = f.readline()
        else:
           fileRead = "false"

        return fileRead

    print(searchFile(str(chatId) + ".txt"))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
executor.start_polling(dp)