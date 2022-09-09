# Imports generales
import asyncio
import re
from pyrogram import Client
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import warnings;warnings.filterwarnings("ignore", category=DeprecationWarning)
loop = asyncio.get_event_loop()

api_id = 5095599
api_hash = "ac087d6bb97a885e4f64571cf7ead8a4"
bot_token1 = '1906762390:AAH0bT5eB_mwBbNiaeHnrjDSbfa_XTt6l48'

bot1 = Client(
    "bot1",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token1,
)




###################################################################################################
# Message Handler:
###################################################################################################
@bot1.on_message()
async def message_handler(client: Client, message: Message):
    if message.text == 'hi':
        await message.reply('hola')

###################################################################################################
# Main Loop
###################################################################################################
print("Starting...")
bot1.start()
print("Online")
loop.run_forever()
