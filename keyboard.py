from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



buttonCute = KeyboardButton('Хочу милую картинку.')
buttonEvil = KeyboardButton('Я злой, не хочу никаких картинок.')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(buttonCute, buttonEvil)
