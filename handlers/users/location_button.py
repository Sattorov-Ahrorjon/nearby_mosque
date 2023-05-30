from aiogram import types
from loader import dp, db
from utils.misc.get_distance import choose_shortest_masjid, choose_shortest_metro
from keyboards import choice_button, location_button


@dp.message_handler(lambda message: message.text in ('Masjid', 'Metro'), state=None)
async def choice(message: types.Message):
    if message.text == "Metro":
        db.update_user_selection(selection='metro', pk=message.from_user.id)
    elif message.text == "Masjid":
        db.update_user_selection(selection="masjid", pk=message.from_user.id)
    await message.answer("Joylashuv malumotingizni yuboring", reply_markup=location_button)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def get_answer(message: types.Message):

    try:
        location = message.location
        closest_shops = ''

        if db.get_selection(message.from_user.id)[0] == 'masjid':
            closest_shops = choose_shortest_masjid(location=location)

        elif db.get_selection(message.from_user.id)[0] == 'metro':
            closest_shops = choose_shortest_metro(location=location)
        text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\nMasofa: {distance:.1f} km."
                            for shop_name, distance, url, shop_location in closest_shops])

        await message.answer(text, disable_web_page_preview=True, reply_markup=choice_button)

        text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\nMasofa: {distance:.1f} km."
                            for shop_name, distance, url, shop_location in closest_shops])
        
        await message.answer(text, disable_web_page_preview=True)
        
        for shop_name, distance, url, shop_location in closest_shops:
            await message.answer_location(latitude=shop_location["lat"], longitude=shop_location["lon"])
    except:
        await message.reply("Joylashuv malumotida xatolik bor !", reply_markup=choice_button)
