import env
from Hack import bot
from Hack.helpers import MENU1, KEYBOARD1
from Hack.database import DB

from telethon import events


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    id = event.sender_id
    mention = f"[{event.sender.first_name}](tg://user?id={id})"
    TEXT = "✇ اهـلا انا بـوت اخـتراق جلـسات 🫧... استطيع اختـراق جلـسات بايروجرام او تيرمكس...ارسـل امـر /Boda"
    await event.reply(TEXT.format(mention))
    if DB:
        await DB.add_user(id)
    if env.LOG_GROUP_ID:
        await bot.send_message(env.LOG_GROUP_ID,
                               f'{mention} هـذا الشخـص بدأ اسـتخدام البـوت')


@bot.on(events.NewMessage(pattern="/Boda"))
async def hack(event):
    if not event.is_private:
        return await event.reply("لا استطيع اختراق الجـلسات هنا ارسل للبوت")
    await event.reply(MENU1, buttons=KEYBOARD1)
