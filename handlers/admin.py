from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой БОСС!!")
        elif not message.reply_to_message:
            await message.answer("Укажи кого банить!")
        else:
            await message.delete()
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан забанил "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

async def game(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не админ, заплати чтоб сыграть в игру!!!")
    else:
        emoji_list = ['⚽', '🏀', '🎯', '🎰', '🎳', '🎲']
        await bot.send_message(message.from_user.id, choice(emoji_list))



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix="!/")
    dp.register_message_handler(game, commands=['game'], commands_prefix="!/")