from ..utils.mysql import mysqlq
from ..utils import BOT
from pyrogram import filters
from random import randint as rand
import json


async def message(msg):
    _MSG, tipo = await get_msg(msg, 1)

    res_msg = await mysqlq(f"SELECT * FROM message WHERE msg = '{_MSG}'")

    if not res_msg:
        await mysqlq(f"INSERT INTO message (msg) VALUES ('{_MSG}')", 1)
        res_msg = await mysqlq(f"SELECT * FROM message WHERE msg = '{_MSG}'")

    return res_msg

async def answer(ans, res_msg):
    _ANS, tipo = await get_msg(ans)

    res_ans = await mysqlq(f"SELECT * FROM answers WHERE answer = '{_ANS}' AND msg_id = {res_msg[0][0]}")
    qtdd = len(await mysqlq(f"SELECT * FROM answers WHERE msg_id = {res_msg[0][0]}"))
    
    if not res_ans and qtdd < 50:
        await mysqlq(f"INSERT INTO answers (answer, msg_id, tipo) VALUES ('{_ANS}', {res_msg[0][0]}, '{tipo}')", 1)
        res_ans = await mysqlq(f"SELECT * FROM answers WHERE msg_id = {res_msg[0][0]}")

    return res_ans

async def get_msg(msg, file_unique_id=False):
    if msg.media:
        tipo = "sticker"
        _str = msg.sticker.file_id if not file_unique_id else msg.sticker.file_unique_id
    else:
        tipo = "text"
        _str = msg.text.replace("\\", "\\\\").replace("'", "\\'").lower()
    
    return _str, tipo

async def add_answer(msg):
    if msg.reply_to_message:
        res_msg = await message(msg.reply_to_message)
        await answer(msg, res_msg)
    
@BOT.on_message((filters.text, filters.sticker))
async def reply_message(_, msg):
    if msg.service:
        return

    await add_answer(msg)

    _MSG = msg.sticker.file_unique_id if msg.media else msg.text.replace("\\", "\\\\").replace("'", "\\'").lower()
    res_msg = await mysqlq(f"SELECT * FROM message WHERE msg = '{_MSG}'")

    if res_msg:
        res_ans = await mysqlq(f"SELECT * FROM answers WHERE msg_id = {res_msg[0][0]}")
        msg_random = rand(0, len(res_ans) - 1)

        send = msg.reply_text if res_ans[msg_random][-1] == "text" else msg.reply_sticker
        await send(res_ans[msg_random][1], quote=True)