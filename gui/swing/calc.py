#!/usr/bin/env jython
from java.awt import FlowLayout
from javax.swing import JFrame, JLabel, JButton
from javax.swing import UIManager
from javax.swing import SwingUtilities


def addBuffer(obj):
    global buffer, bufferlabel
    char = obj.getSource().getText()
    buffer+=char
    bufferlabel.setText(buffer)

def addOper(obj):
    global buffer, bufferlabel
    char = obj.getSource().getText()
    if len(buffer) == 0:
        pass
    else:
        if buffer[-1] in ["+", "-", "*", "/"]:
            buffer = buffer[:-1] + char
        else:
            buffer += char
            bufferlabel.setText(buffer)

def result():
    global buffer, bufferlabel
    print (buffer)
    if '+' in buffer or '-' in buffer or '*' in buffer or '/' in buffer:
            buffer = str(eval(buffer))
            bufferlabel.setText(buffer)
    else:
        pass

string=["Calculadora sovietica"]
buffer = ""
title = JLabel(string[0])
title.setBounds(0, 0, 200, 15)

bufferlabel = JLabel()
bufferlabel.setBounds(0, 30, 400, 15)
buttons = [
    ["1", 1], ["2", 1], ["3", 1], ["+", 0], ["-", 0],
    ["4", 1], ["5", 1], ["6", 1], ["*", 0], ["/", 0],
    ["7", 1], ["8", 1], ["9", 1], ["0", 1], ["=", 3]
]
d = {}
x = 0
y = 60
count = 0
for button in buttons:
    if count == 5:
        count = 0
        y += 40
        x = 0
    d[button[0]] = JButton(button[0])
    d[button[0]].setBounds(x, y, 55, 35)
    if button[-1] == 1:
        d[button[0]].addActionListener(lambda x: addBuffer(x))
    if button[-1] == 0:
        d[button[0]].addActionListener(lambda x: addOper(x))
    if button[-1] == 3:
        d[button[0]].addActionListener(lambda x: result())
    x += 60
    count +=1


frame = JFrame()
frame.setLayout(None)
frame.setTitle(string[0])
frame.add(title)
frame.add(bufferlabel)

for button in d.keys():
    frame.add(d[button])

frame.setBounds(10, 10, 300, 200)
frame.setVisible(True)
frame.setResizable(False)
LAF="com.sun.java.swing.plaf.motif.MotifLookAndFeel"
#LAF="javax.swing.plaf.metal.MetalLookAndFeel"
#LAF="javax.swing.plaf.nimbus.NimbusLookAndFeel"
#LAF="com.sun.java.swing.plaf.gtk.GTKLookAndFeel"
UIManager.setLookAndFeel(LAF)
SwingUtilities.updateComponentTreeUI(frame)