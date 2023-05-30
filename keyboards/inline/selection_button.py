from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

selection = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Masjid', callback_data='masjid'),
            InlineKeyboardButton(text='Metro', callback_data='metro')
        ],
    ],
)
