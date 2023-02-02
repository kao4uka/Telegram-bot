from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import bot, ADMINS
from database.bot_db import sql_command_random, sql_command_delete
from keyboards.client_kb import start_markup
from parsers.anime import parser


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Привет, {message.from_user.first_name}",
                           reply_markup=start_markup)


async def info_handler(message: types.Message):
    await message.answer("Сам разбирайся!")


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

async def get_random_user(message: types.Message):
    random_mentor = await sql_command_random()
    markup = None
    if message.from_user.id in ADMINS:
        markup = InlineKeyboardMarkup().add(
            InlineKeyboardButton(f"delete {random_mentor[1]}",
                                 callback_data=f"delete {random_mentor[0]}"))
    await message.answer(
        random_mentor[0],
        f"Имя: {random_mentor[1]}\nВозраст: {random_mentor[2]}\n"
        f"Направление: {random_mentor[3]}\nГруппа: {random_mentor[4]}",
        reply_markup=markup)

async def pin(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id,  message.reply_to_message.message_id)
    else:
        await message.answer("Укажи кого закрепить!!!")

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text="Deleted!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)

async def get_movie(message: types.Message):
    movie = parser()
    for i in movie:
        await message.answer(
            f"{i['link']}\n\n"
            f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
            f"{i['info']}\n",
            parse_mode=ParseMode.HTML
        )





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!")
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))
    dp.register_message_handler(get_movie, commands=['movie'])