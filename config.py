import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "20445864"))
API_HASH = os.getenv("API_HASH", "aef4167a97c855cf4775935fa35d0922")
SESSION = os.getenv("BQE3-qgAWm6Mh-d5-f5lX7BzJp_ywYMEgQTDaWcatP_ySxQMo3AJvYlehqAxbVzzf9pdl5CuSsIuxS-eH4PCC5XKkHXIbopTU8wcsvuqxnJzh0kI7BaRtkgmKqZGbRdF0wlwFrznnnnMLI8JVIhGqK1CYNazXo46Kr4zIumZ4c_vB5U0svsUHUbRRM2u2vk6UdFYe2Fa9IIAIPnk8cHzi1P-UZ8AVXvjeHscrCSyDbxOknfiBedez8SAVNisuYK6_OgszQMdTQSpQYU2bi03jbSf9lWFUMmfZ7HXXht5bL6hj5Lfc8GfkHiii6zUeqrg-KL_lJDItSpshx9m-TT-G6EgjzJrDwAAAAHp5VvlAQ")
HNDLR = os.getenv("HNDLR", "8308121662")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
