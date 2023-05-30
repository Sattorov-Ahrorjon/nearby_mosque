from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, db
from data.config import ADMINS
from keyboards import choice_button
# from aiogram.utils.markdown import hlink


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.get_user(pk=message.from_user.id):
        db.add_user(pk=message.from_user.id, name=message.from_user.first_name)
        for admin in ADMINS:
            text = "Yangi foydalanuvchi qo'shildi"
            if not message.from_user.username:
                text += f"\nUsername \\- [{message.from_user.full_name}](tg://user?id={message.from_user.id})"
                text += f"\nID \\- {message.from_user.id}"
                await bot.send_message(chat_id=admin, text=text, parse_mode=types.ParseMode.MARKDOWN_V2)
            else:
                text += f"\nUsername - @{message.from_user.username}"
                text += f"\nID - {message.from_user.id}"
                await bot.send_message(chat_id=admin, text=text, parse_mode=types.ParseMode.HTML)

    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!")
    await bot.send_message(chat_id=message.from_user.id,
                           text="Menga joylashuv manzilingizni yuboring\n"
                                "Men sizga eng yaqin joylashuv haqida malumot beraman",
                           reply_markup=choice_button)

    # await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")
    # await bot.send_message(chat_id=message.from_user.id,
    #                        text="Menga joylashuv manzilingizni yuboring\n"
    #                             "Men sizga eng yaqin Metro bekati haqida malumot beraman",
    #                        reply_markup=choice_button)

    # msg = hlink(message.from_user.full_name, f'tg://openmessage?user_id={message.chat.id}')
    # if message.from_user.username:
    #     await bot.send_message(chat_id=ADMINS[0], text=f"@{message.from_user.username}")
    # else:
    #     await bot.send_message(chat_id=ADMINS[0], text=msg)
    #
    # await message.answer(f"[{message.from_user.full_name}](tg://user?id={message.from_user.id})",
    #                      parse_mode=types.ParseMode.MARKDOWN_V2)
