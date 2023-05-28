from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Сколько будет 66+44?"
    answers = [
        '[100]',
        '[110]',
        '[100,10]',
        '[1010]',
        '[+-100]',
    ]

    photo = open("mems/cartinka.png", 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=60,
        reply_markup=markup
    )
# @dp.callback_query_handler(text='button_call_2')
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT", callback_data='button_call_3')
    markup.add(button_call_3)
    question = "Cколько планет в Солнечной системе?"
    answers =[
        '8',
        '9',
        '10',
        '11',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        type='quiz',
        is_anonymous=False,
        correct_option_id=0,
        open_period=15,
        reply_markup=markup
    )

# @dp.callback_query_handler(text='button_call_3')
async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("NEXT", callback_data='button_call_4')
    markup.add(button_call_4)
    question = "Какое животное не фигурирует в китайском зодиаке?"
    answers =[
        'Дракон',
        'Кролик',
        'Колибри',
        'Собака',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        type='quiz',
        is_anonymous=False,
        correct_option_id=2,
        open_period=15,
        reply_markup=markup
    )
# @dp.callback_query_handler(text='button_call_4')
async def quiz_5(call: types.CallbackQuery):
    question = "Fe — это символ какого химического элемента??"
    answers =[
        'Цинк',
        'Водород',
        'Железо',
        'Фтор',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        type='quiz',
        is_anonymous=False,
        correct_option_id=2,
        open_period=15,
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3, text="button_call_2")
    dp.register_callback_query_handler(quiz_4, text="button_call_3")
    dp.register_callback_query_handler(quiz_5, text="button_call_4")