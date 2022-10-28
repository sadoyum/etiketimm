# Botunu aşağıdaki link'e belirt veya configs e BOT_USERNAME şeklinde belirt keyfine göre yeğenim :) 
# Telegram da beni bulmak için @Mahoaga die arat sizlere yardımcı olabilirim. 
# Sadece hobi amaçlı yapılan bir deneme projesidir. 

from Plugins import Maho
from telethon import events, Button
from telethon.tl.types import ChannelParticipantsAdmins

@Maho.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await Maho.send_message(-1001210894866, f"ℹ️ **Start Veren Kullanıcı -** {ad}")
     return await event.reply(f"**Merhaba\nBenim Görevim Üyeleri Etiketlemektir.\nKomutlar için Komutlar butonuna basınız.**", buttons=(
                      [
                       Button.inline("Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Gruba Ekle', 'http://t.me/Sensizolmaz_bot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/TaliaSupport')
                      ],
                      [
                       Button.url('🇹🇷 Sahibim', 'https://t.me/Mahoaga')
                      ],
                    ),
                    link_preview=False)


  if event.is_group:
    return await Maho.send_message(event.chat_id, f"**Beni Grubuna Aldığın için Teşekkürler ✨**")

# Başlanğıc Button
@Maho.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in Maho.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**Merhaba Benim adım Tagger\nGörevim Üyeleri Etiketlemek\nKomutlar için Komutlar Düğmesine Basın.**", buttons=(
                      [
                       Button.inline("Komutlar", data="komutlar")
                      ],
                      [
                       Button.url('↘️ Gruba Ekle', 'http://t.me/Sensizolmaz_bot?startgroup=a'),
                       Button.url('📣 Kanal', 'https://t.me/TaliaSupport')
                      ],
                      [
                       Button.url('🇹🇷 Sahibim', 'https://t.me/Mahoaga')
                      ],
                    ),
                    link_preview=False)

# Maho aga
@Maho.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"**Komutlarım:\n\n/tag Toplu etiket atar..\n/yt Sadece yöneticileri etiketlemek içindir.\n/ttag Tek tek etiketleme yapar.\n/btag Bayraklar ile etiketlemek içindir.\n/stag Sözler ile etiketler.\n/itag İsimler ile etiketlemek içindir.\n/futbol Futbolcu isimleri ile etiketleme.\n/etag Emojiler ile etiketleme işlemidir.\n/cancel - Sonlandırır... \n\n❗ Yalnızca yöneticiler bu komutları kullanabilir.**", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)
