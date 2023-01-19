from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from keyboards.client_kb import start_markup


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Привет, {message.from_user.first_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method")
    # await message.reply("This is a reply method")


async def info_handler(message: types.Message):
    await message.answer("Сам разбирайся!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какая река самая длинная в мире?"
    answers = [
        "Нил",
        "Амазонка",
        "Миссисипи",
        "Енисей",
        "Нарын",
        "Волга",
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        reply_markup=markup
    )

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id,  message.reply_to_message.message_id)
    else:
        await message.answer("Укажи кого закрепить!!!")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")

