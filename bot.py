from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from config import TOKEN
import keyboard as key

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=key.mainMenu)

@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == 'Хочу милую картинку.':
        img = open('cat.jpg', 'rb')
        await bot.send_photo(msg.from_user.id, img, 'Держи милую картинку!')
    elif msg.text == 'Я злой, не хочу никаких картинок.':
        await bot.send_message(msg.from_user.id, 'Уходи отсюда тогда...')

if __name__ == '__main__':
    executor.start_polling(dp)