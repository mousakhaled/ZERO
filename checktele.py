import random
import asyncio
import telethon
from telethon import events
from queue import Queue
import requests
from telethon.sync import functions
from user_agent import generate_user_agent
import requests
from user_agent import *
from help import *
from config import *
from threading import Thread

a = 'qwertyuiopasdfghjklzxcvbnm'
b = '1234567890'
e = 'qwertyuiopasdfghjklzxcvbnm1234567890'
oo = 'qwertyuiopasdfghkjlzxxcvbnm1234567890'
z = 'xozsav'
zz = 'qwertyuiopasdfhklzxcvbnm'
aa = 'wertyuiopasdfhklzxcvbnm'
ss = 'xdj'
xxxx = 'xx'
pppp = 'pp'
cw = 'weruoiaszxcvnm'
cv = 'weruoiaszxcvnm'
co = 'weruoiaszxcvnm'
v = "aslzxcvnioouytre"
vv = "aszxcvneor"
vvv = "lisxjfczverouq"

isclaim = ["off"] 
isauto = ["off"]
xxxxx = [
'xxxxp',
'xxxxz',
]
que = Queue()


def check_user(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "Available"
    else:
        return "Unavailable"


def gen_user(choice):
    if choice == "1":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", d[0]]
        username = ''.join(f)
    if choice == "2":
        c = random.choices(v)
        d = random.choices(vv)
        s = random.choices(vvv)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
    if choice == "3":
        c = d = random.choices(a)
        d = random.choices(zz)
        f = [c[0], c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(zz)
            f = [c[0], c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "4":
        c = random.choices(a)
        d = random.choices(zz)
        s = random.choices(oo)
        f = [c[0], s[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(zz)
            s = random.choices(oo)
            f = [c[0], s[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    if choice == "5":
        c = d = random.choices(a)
        d = random.choices(oo)
        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(oo)
            f = [c[0], d[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "6":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(b)
            f = [c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
    if choice == "7":
        c = d = random.choices(a)
        d = random.choices(zz)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
        if username in banned[0]:
            c = d = random.choices(a)
            d = random.choices(zz)
            f = [c[0], c[0], c[0], c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
    if choice == "8":
        c = random.choices(a)
        d = random.choices(zz)
        s = random.choices(e)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
    if choice == "9":
        c = random.choices(ss)
        f = [c[0], c[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = ''.join(f)
    if choice == "0":
        c = random.choices(a)
        d = random.choices(aa)
        f = [c[0], "_", d[0], "_", d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(aa)
            f = [c[0], "_", d[0], "_", d[0]]
            random.shuffle(f)
            username = ''.join(f)
        else:
            pass
    if choice == "10":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", c[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "11":
        c = random.choices(a)
        s = random.choices(zz)
        f = [c[0], "_", d[0], "_", d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(zz)
            f = [c[0], "_", d[0], "_", d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "12":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], "_", d[0], "_", d[0]]
        username = ''.join(f)
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            f = [c[0], "_", d[0], "_", d[0]]
            username = ''.join(f)
        else:
            pass
    if choice == "13":
        c = random.choices(cw)
        d = random.choices(cv)
        s = random.choice(co)
        f = [c[0], "_", d[0], "_", s[0]]
        username = ''.join(f)
    if choice == "14":
        c = random.choices(a)
        d = random.choices(b)
        f = [c[0], d[0]]
        random.shuffle(f)
        username = ''.join(f)
        username = username+'bot'
        if username in banned[0]:
            c = random.choices(a)
            d = random.choices(b)
            f = [c[0], d[0]]
            random.shuffle(f)
            username = ''.join(f)
            username = username+'bot'
        else:
            pass
    return username


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.تشيكر تلي"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.اليوزرات المبندة"))
async def _(event):
    if ispay2[0] == "yes":
        await xdexer.send_file(event.chat_id, 'banned.txt')
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.الانواع"))
async def _(event):
    if ispay2[0] == "yes":
        await event.edit(tele_checker2)
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


# كلايم عدد نوع قناة


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.كلايم (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        isclaim.clear()
        isclaim.append("on")
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 2)
        ch = str(msg[2])
        choice = str(msg[1])
        
        await event.edit(f"حسناً سأفحص نوع `{choice}` من اليوزرات على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

        @xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.حك"))
        async def _(event):
            if ispay2[0] == "yes":
                if "on" in isclaim:
                    await event.edit(f"  الكلايم يعمل!  ")
                elif "off" in isclaim:
                    await event.edit("لايوجد كلايم شغال !")
                else:
                    await event.edit("خطأ")
            else:
                pass
        for i in range(int(msg[0])):
            if ispay2[0] == 'yes':
                break
            username = ""

            username = gen_user(choice)
            t = Thread(target=lambda q, arg1: q.put(
                check_user(arg1)), args=(que, username))
            t.start()
            t.join()
            isav = que.get()
            if "Available" in isav:
                await asyncio.sleep(1)
                try:
                    await xdexer(functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username))
                    await event.client.send_message(event.chat_id, f'''
**Hey BATZ & VOLT,
i Catch new User!
- User: @{username} 🎯
- Source: #ZERO**
''')


                    break
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    with open("banned.txt", "a") as f:
                        f.write(f"\n{username}")
                except Exception as eee:
                    await xdexer.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                    if "A wait of" in str(eee):
                        break
                    else:
                        await xdexer.send_message(event.chat.id, "سأستمر بلفحص !")
            else:
                pass
            

        isclaim.clear()
        isclaim.append("off")
        
        await event.client.send_message(event.chat_id, "تم الانتهاء من الفحص")
    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")


@xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.تثبيت (.*)"))
async def _(event):
    if ispay2[0] == "yes":
        
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if msg[0] == "تلقائي":  # تثبيت تلقائي عدد يوزر قناة
            isauto.clear()
            isauto.append("on")
            msg = ("".join(event.text.split(maxsplit=2)[2:])).split(" ", 2)
            username = str(msg[2])
            ch = str(msg[1])
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` , بعدد `{msg[0]}` من المحاولات !")

            @xdexer.on(events.NewMessage(outgoing=True, pattern=r"\.حالة التثبيت التلقائي"))
            async def _(event):
                if "on" in isauto:
                    msg = await event.edit(f"يعمل")
                elif "off" in isauto:
                    await event.edit("لايوجد تثبيت شغال !")
                else:
                    await event.edit("خطأ")
            for i in range(int(msg[0])):
                if ispay2[0] == 'yes':
                    break
                t = Thread(target=lambda q, arg1: q.put(
                    check_user(arg1)), args=(que, username))
                t.start()
                t.join()
                isav = que.get()
                if "Available" in isav:
                    try:
                        await xdexer(functions.channels.UpdateUsernameRequest(
                            channel=ch, username=username))
                        await event.client.send_message(event.chat_id, f'''
**Hey BATZ & VOLT,
i Catch new User!
- User: @{username} 🎯
- Source: #ZERO**
''')



                        break
                    except telethon.errors.rpcerrorlist.UsernameInvalidError:
                        await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
                        break
                    except Exception as eee:

                        await xdexer.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')
                        if "A wait of" in str(eee):
                            break
                else:
                    pass
                

                await asyncio.sleep(8)
            
            isclaim.clear()
            isclaim.append("off")
            await xdexer.send_message(event.chat_id, "تم الانتهاء من التثبيت التلقائي")
        if msg[0] == "يدوي":  # تثبيت يدوي يوزر قناة
            await event.edit(f"حسناً سأحاول تثبيت `{username}` على `{ch}` !")
            msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
            username = str(msg[0])
            ch = str(msg[1])
            try:
                await xdexer(functions.channels.UpdateUsernameRequest(
                    channel=ch, username=username))
                await event.client.send_message(event.chat_id, f'''        
**Hey BATZ & VOLT,
i Catch new User!
- User: @{username} 🎯
- Source: #ZERO**
''')


            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                await event.client.send_message(event.chat_id, f"مبند `{username}` ❌❌")
            except Exception as eee:
                await xdexer.send_message(event.chat_id, f'''خطأ مع {username}
    الخطأ :
    {str(eee)}''')

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
