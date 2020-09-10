import socket as ss
import net # for global vars use ;)

ADDRESS = ( "127.0.0.1",37111 )

class Server():
    def __init__(self):
        #create socket object
        self.s = ss.socket()
        self.s.bind(net.ADDRESS)
        self.s.listen(0)
    def accept(self):
        client, address = self.s.accept()
        return client, address


