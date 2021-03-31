import smtplib
class Mailer(smtplib.SMTP):
    def __init__(self, host="181.225.231.12", port=25, user="", passwd=""):
        self.user = user
        self.object = smtplib.SMTP(host, port)
        check= self.object.login(user,passwd)
        if check[1] != b'2.7.0 Authentication successful' :
            print("Error authenticating")
            exit(1)
        pass
    def send(self, to=[], subject="", body=""):
        check = self.object.sendmail(self.user, [to], f"FROM: {self.user}\nTO: {to}\nSUBJECT: {subject}\n\n{body}")
        #print ("Success") if check == {} else print ("Destinatary unreachable")
        return check