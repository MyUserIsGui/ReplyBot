from pyrogram import Client
from ..vars import var


BOT = Client(
    session_name = "bot",
    api_id = var.API_ID, 
    api_hash = var.API_HASH,
    bot_token = var.BOT_TOKEN,
)