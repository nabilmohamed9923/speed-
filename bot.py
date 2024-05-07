import pyrogram , pyromod

from pyrogram import Client, filters, enums
from kvsqlite.sync import Client as dt
p = dict(root='plugins')
tok = '7096739598:AAG2hCcreOGaR7dA-yh-CKqGpoBwiwqgtH8' ## توكنك 
id = 6531677413 ## ايديك
db = dt("data.sqlite", 'fuck')
if not db.get("checker"):
  db.set('checker', None)
if not db.get("admin_list"):
  db.set('admin_list', [id, 6531677413])
if not db.get('ban_list'):
  db.set('ban_list', [])
if not db.get('sessions'):
  db.set('sessions', [])
if not db.get('force'):
  db.set('force', ['source_ze'])
x = Client(name='loclhosst', api_id=26615390, api_hash='bcb38874b8b863d3f52f526fd91515b6', bot_token=tok, workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)

x.run()
