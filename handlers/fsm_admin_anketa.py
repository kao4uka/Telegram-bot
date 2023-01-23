from aiogram.dispatcher.filters.state import State, StatesGroup
from database.bot_db import sql_command_insert
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from keyboards import client_kb
from config import ADMINS
import uuid

class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    age = State()
    direction = State()
    group = State()
    submit = State()
async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.from_user.id in ADMINS:
        await FSMAdmin.name.set()
        await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Ты кто?")


async def load_name(message: types.Message, state: FSMContext):
    UID = uuid.uuid1()
    async with state.proxy() as data:
        data['id'] = int(UID)
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Cколько лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 16 < int(message.text) < 70:
        await message.answer("Доступ ограничен!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какое направление?")

async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Какая группа?')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await message.answer(f"ID: {data['id']}\nИмя: {data['name']}\nВозраст: {data['age']}\n"
                         f"Направление: {data['direction']}\nГруппа: {data['group']}"
                         )
    await FSMAdmin.next()
    await message.answer("Все верно?",
                         reply_markup=client_kb.submit_markup)


async def load_submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Регистрация завершена!', reply_markup=client_kb.start_markup)
    elif message.text.lower() == "Изменить":
        await FSMAdmin.name.set()
        await message.answer("Имя ментора?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer('Нипонял!?')

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Canceled")

def register_handlers_admins(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(load_submit, state=FSMAdmin.submit)
