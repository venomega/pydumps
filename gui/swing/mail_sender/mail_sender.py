#!/usr/bin/env jython
from java.awt import Color
from javax.swing import *
from javax.swing import UIManager
from javax.swing import SwingUtilities

from mailer import Mailer

class win(JFrame):
    def __init__(self, title="Mail Sender"):
        JFrame(title)
        self.setLayout(None)
        self.setBounds(10, 10, 400, 350)
        self.show()
        self.build()

    def build(self):
        luser = JLabel("Username:")
        token = len(luser.getText())*8
        luser.setBounds(10, 10, token, 15)
        self.tuser = JTextField()
        self.tuser.setBounds(token + 12, 10, 100, 20)
        lpasswd = JLabel("Passwd:")
        token2 = len(lpasswd.getText())
        lpasswd.setBounds(token + 12 + 120, 10, token, 20)
        self.tpasswd = JTextField()
        self.tpasswd.setBounds(token2 + token + 180, 10, 100, 20)
        self.body= JTextArea()
        scroll = JScrollPane(self.body)
        scroll.setBounds(10, 40, 390, 240)
        self.body.setBackground(Color(255,255,255))
        button = JButton("Enviar")
        button.setBounds(140, 290, 100, 30)
        button.addActionListener(lambda x: self.send())
        for var in [luser,self.tuser, lpasswd, self.tpasswd, scroll, button]:
            self.add(var)

    def send(self):
        body = self.body.getText()
        user = self.tuser.getText()
        passwd = self.tpasswd.getText()
        o = Mailer(user=user, passwd=passwd)
        if o.send(to="guilleps92@gmail.com", subject="Jython", body=body) == {}:
            self.body.setText("")
        else:
            pass
o = win()

LAF="com.sun.java.swing.plaf.motif.MotifLookAndFeel"
UIManager.setLookAndFeel(LAF)
SwingUtilities.updateComponentTreeUI(o)