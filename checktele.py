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
a = "qwertyuiopassdfghjklzxcvbnm"
b = "1234567890"
e = "qwertyuiopasdfghjklzxcvbnm"
v = "aslzxcvnioouytre"
vv = "aszxcvneor"
vvv = "lisxjfczverouq"
x = "fglityqpmb"
xx = "zxcvnmasero"
cc = "iqdh"
ccc = "fgjklzxcwertyuopasvbnm4567012389"
trys, trys2 = [0], [0]
isclaim = ["off"]
isauto = ["off"]


def check_user(username):
    url = "https://t.me/" + str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    response = requests.get(url, headers=headers)
    if (
        response.text.find(
            'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"'
        )
        >= 0
    ):
        return True
    else:
        return False


def gen_user(choice):
    if choice == "مكرر":
        c = random.choices(x)
        d = random.choices(xx)
        f = [c[0], "_", d[0], "_", d[0]]
        username = "".join(f)

    elif choice == "ثلاثيات":
        c = random.choices(v)
        d = random.choices(vv)
        s = random.choices(vvv)
        f = [c[0], "_", d[0], "_", s[0]]
        username = "".join(f)
    elif choice == "سداسيات":
        c = d = random.choices(cc)
        d = random.choices(ccc)
        f = [c[0], d[0], c[0], c[0], c[0], c[0]]
        username = "".join(f)
    elif choice == "بوتات":
        c = random.choices(v)
        d = random.choices(vv)
        s = random.choices(vvv)
        f = [c[0], s[0], d[0]]
        # random.shuffle(f)
        username = "".join(f)
        username = username + "bot"

    elif choice == "خماسي حرفين":
        c = random.choices(xx)
        d = random.choices(x)

        f = [c[0], d[0], c[0], c[0], d[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "خماسي":
        c = random.choices(cc)
        d = random.choices(ccc)
        f = [c[0], d[0], c[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)

    elif choice == "سباعيات":
        c = d = random.choices(a)
        d = random.choices(b)
        f = [c[0], c[0], c[0], c[0], d[0], c[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    elif choice == "تيست":
        c = d = random.choices(a)
        d = random.choices(b)
        s = random.choice(xx)
        f = [c[0], d[0], c[0], s[0], d[0], c[0]]
        random.shuffle(f)
        username = "".join(f)
    else:
        return "error"
    return username
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
async def hunterusername(event):
    msg = event.text.split()
    choice = str(msg[1])
    try:
        ch = str(msg[2])
        if "@" in ch:
            ch = ch.replace("@", "")
        await event.edit(f"حسناً سيتم بدء الصيد في @{ch} .")
    except:
        try:
            ch = await jmub(
                functions.channels.CreateChannelRequest(
                    title="#ZERO ",
                    about="This User is Claimed by #ZERO 🦖",
                )
            )
            ch = ch.updates[1].channel_id
            await event.edit(f"**- تم تفعيل الصيد بنجاح الان**")
        except Exception as e:
            await jmub.send_message(
                event.chat_id, f"خطأ في انشاء القناة , الخطأ**-  : {str(e)}**"
            )
    isclaim.clear()
    isclaim.append("on")
    for i in range(19000000):
        username = gen_user(choice)
        if username == "error":
            await event.edit("**- يرجى وضع النوع بشكل صحيح**.")
            break
        isav = check_user(username)
        if isav == True:
            try:
                await jmub(
                    functions.channels.UpdateUsernameRequest(
                        channel=ch, username=username
                    )
                )
                await event.client.send_message(
                    event.chat_id,
                    f"- Done: @{username} 🎯!\n- By: #ZERO !\n- Attempts: {trys2[0]}",
                )
                break
            except telethon.errors.rpcerrorlist.UsernameInvalidError:
                pass
            except Exception as baned:
                if "(caused by UpdateUsernameRequest)" in str(baned):
                    pass
            except telethon.errors.FloodError as e:
                await jmub.send_message(
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                    event.chat_id,
                    f"للاسف تبندت , مدة الباند**-  ({e.seconds}) ثانية .**",
                )
                break
            except Exception as eee:
                if "the username is already" in str(eee):
                    pass
                else:
                    await jmub.send_message(
                        event.chat_id,
                        f"""- خطأ مع @{username} , الخطأ :{str(eee)}""",
                    )
                    break
        else:
            pass
        trys[0] += 1
    isclaim.clear()
    isclaim.append("off")
    await event.client.send_message(event.chat_id, "**- تم بنجاح الانتهاء من الصيد**")



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