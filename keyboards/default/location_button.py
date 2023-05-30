from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

choice_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Masjid")
        ],
        [
            KeyboardButton(text="Metro")
        ]
    ],
    resize_keyboard=True
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Location", request_location=True)
        ]
    ],
    resize_keyboard=True
)
