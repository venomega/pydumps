import json
import storage # for global vars support
p_nick="./nick.json"
d = {}
try:
    open(p_nick,"r").read()
except:
    open(p_nick,"w").write("")

def _save_nick(nick,addr):
    json.load(storage.d,storage.p_nick)
    storage.d[nick] = address
    json.dump(storage.d,storage.p_nick)
def load():
    json.load(storage.d,storage.p_nick)
def put_nick(nick,address):
    _save_nick(nick,address)


