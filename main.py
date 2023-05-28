from aiogram.utils import executor
import logging
from config import dp, bot, ADMINS
from handlers import client, callback, extra, admin, fsm_admin_anketa, notification
from database.bot_db import sql_create
from audio_converter import video_to_audio
import asyncio

async def on_sturtup(_):
    asyncio.create_task(notification.scheduler())
    sql_create()
    await bot.send_message(chat_id=ADMINS[0],
                           text="Bot started!")



client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
fsm_admin_anketa.register_handlers_admins(dp)
notification.register_handlers_notification(dp)
video_to_audio.register_handlers(dp)


extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_sturtup)
