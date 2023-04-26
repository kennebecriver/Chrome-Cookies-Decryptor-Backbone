# based on https://tek4.vn/cach-giai-nen-cookie-cua-chrome-bang-python
import os
import json
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import base64
from datetime import datetime

appdata_path = os.environ['LOCALAPPDATA']
cookies_path = os.path.join(appdata_path, 'Google\\Chrome\\User Data\\Default\\Network\\Cookies')
local_state_path = os.path.join(appdata_path, 'Google\\Chrome\\User Data\\Local State')

with open(local_state_path, "r", encoding="utf-8") as f:
    key = base64.b64decode(json.loads(f.read())["os_crypt"]["encrypted_key"])[5:]
encryption_key = win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

conn = sqlite3.connect(cookies_path)
cursor = conn.cursor()
cursor.execute('SELECT name, encrypted_value, host_key FROM cookies')

result = ""
for row in cursor.fetchall():
    data = row[1]
    cipher = AES.new(encryption_key, AES.MODE_GCM, data[3:15])
    value = cipher.decrypt(data[15:])[:-16].decode()
    result += f"{row[2]}; {row[0]}={value};\n"
    break
print(result)

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
with open(f"chrome_cookies_result_{now}.txt", "w", encoding="utf-8") as f:
    f.write(result)

print(f"Done: {now}")
