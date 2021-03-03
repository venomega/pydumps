#!/usr/bin/env python3
import os
import sys
import time

# ESTE SCRIPT FUNCIONA TANTO PARA WINDOWS COMO PARA LINUX


if sys.platform == "linux":
    if os.system("/usr/bin/touch /usr/bin/mpv") == 0:
        reproductor = "mpv --vo=x11 "
    else:
        reproductor = "xdg-open "
else:
    reproductor = "start "

banner0 ="""
TV VIEWIER 
para la red interna de la uci
PD(hasta el momento)
hecho por alguien que no sabe nada
"""
banner1 = """
1 - cubavision
2 - multivision
3 - tele rebelde
4 - telesur
5 - cuba internacional
6 - clave

0 - Salir
"""

class Channel(object):
    def __init__(self):
        URL=""
    def play(self, str):
        global reproductor
        os.system(f"{reproductor} {str}")
    def cubavision(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch6"
        self.play(self.URL)
    def rebelde(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch2"
        self.play(self.URL)
    def multivision(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch11"
        self.play(self.URL)
    def telesur(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch5"
        self.play(self.URL)
    def internacional(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch12"
        self.play(self.URL)
    def clave(self):
        self.URL = "mms://ucimedia.uci.cu/e7dd297dch13"
        self.play(self.URL)


        
def caller(self):
    if self == 1:
        a = Channel()
        a.cubavision()
    if self == 2:
        Channel.multivision()
    if self == 3:
        Channel.rebelde()
    if self == 4:
        Channel.telesur()
    if self == 5:
        Channel.internacional()
    if self == 6:
        Channel.clave()
    if self == 0:
        exit(0)

        
def error(self):
    print ("Error: " + self)
    sys.exit(-1)
    
def handler(self):
    if self < 1 or self > 6:
        error(" menu")
    else:
        caller(self)
    
def main():
    channel=Channel()
    print(banner0)
    while True:
        print (banner1)
        hola = int (input("Elija un canal a reproducir: "))
        handler(hola)

        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(error(" keyboard"))
    except ValueError:
        sys.exit(error(" menu"))
