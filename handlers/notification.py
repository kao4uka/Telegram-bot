import aioschedule
import asyncio
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = list()
    chat_id.append(message.from_user.id)
    await message.answer("OK")


async def go_to_gym():
    for id in chat_id:
        await bot.send_message(id, "Пора тренироваться!")


async def scheduler():
    aioschedule.every().monday.at("10:00").do(go_to_gym)
    aioschedule.every().thursday.at("11:00").do(go_to_gym)
    aioschedule.every().saturday.at("9:00").do(go_to_gym)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "напомни" in word.text)
