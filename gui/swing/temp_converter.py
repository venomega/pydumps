from javax.swing import JFrame, JLabel, JButton, JTextField
from javax.swing import UIManager
from javax.swing import SwingUtilities


def log(x):
    help(x)


class oper():

    def from_celcius(self, num):
        #farenheit
        f = round((lambda x: (x*1.8)+32) (num), 2)
        k = round((lambda x: x+273.15) (num), 2)
        return [f, k]

    def from_farenheit(self, num):
        #farenheit
        c = round((lambda x: (x-32)*5/9) (num), 2)
        k = round((lambda x: c+273.15) (num), 2)
        return [c, k]

    def from_kelvin(self, num):
        #farenheit
        c = round((lambda x: x-273.15) (num), 2)
        f = round((lambda x: (c*1.8)+32) (num), 2)
        return [f, c]


class win(JFrame):
    def __init__(self, title="Convertidor Temp"):
        JFrame(title)
        self.setLayout(None)
        self.setBounds(10, 10, 300, 180)
        self.show()
        self.build()

    def build(self):
        #labels
        cl = JLabel("Celcius")
        cl.setBounds(10, 10, 60, 20)
        fl = JLabel("Farenheit")
        fl.setBounds(120, 10, 60, 20)
        kl = JLabel("Kelvin")
        kl.setBounds(230, 10, 60, 20)
        #celcius textfield
        c = JTextField()
        c.setBounds(10, 40, 60, 20)
        c.addActionListener(lambda x: log(x))
        #farenheit textfield
        f = JTextField()
        f.setBounds(120, 40, 60, 20)
        f.addActionListener(lambda x: log(x))
        #kelvin textfield
        k = JTextField()
        k.setBounds(230, 40, 60, 20)
        k.addActionListener(lambda x: log(x))
        #buttons
        cv=JButton("Convert")
        cv.addActionListener(lambda x: self.convert(x))
        cv.setBounds(10, 70, 300 - 10, 30)
        clean=JButton("Clean")
        clean.addActionListener(lambda x: self.clean())
        clean.setBounds(10, 110, 300 - 10, 30)
        #add vars to frame
        list(map(lambda x: self.add(x), [cl,kl,fl,c,f,k,cv,clean]))
        self.k = k
        self.c = c
        self.f = f
        self.textfields={self.c, self.f, self.k}

    def clean(self):
        list(map(lambda x: x.setText(""), self.textfields))

    def convert(self, x):
        token = self.textfields
        for var in token:
            if var.getText() == "":
                token = token - {var}
        if len(token) == 1:
            try:
                num = float(list(token)[0].getText())
            except:
                pass
            o = oper()
            x = list(token)[0]
            if x == self.c:
                f, k = o.from_celcius(num)
                self.f.setText(str(f)), self.k.setText(str(k))
            if x == self.f:
                a = o.from_farenheit(num)
                self.c.setText(str(a[0])), self.k.setText(str(a[1])) 
            if x == self.k:
                f, c = o.from_kelvin(num)
                self.f.setText(str(f)), self.c.setText(str(c)) 
                
        
o = win()
#// Look and Feel
LAF="com.sun.java.swing.plaf.motif.MotifLookAndFeel"
UIManager.setLookAndFeel(LAF)
SwingUtilities.updateComponentTreeUI(o)