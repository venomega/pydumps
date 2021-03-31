#!/usr/bin/env jython
from java.awt import FlowLayout
from javax.swing import JFrame, JLabel, JButton, JTextField
from javax.swing import UIManager
from javax.swing import SwingUtilities

def calculate(val):
    try:
        val = int(val)
    except:
        pass
    ranges = []
    total = 0
    fd = open("table.txt").read().split('\n')
    for line in fd:
        asd = line.split()
        if len(asd) > 3:
            low, high = asd[1].split('-')
            price = float(asd[-1][1:])
            ranges.append([int(low), int(high), price])
        else:
            pass

    for rang in ranges:
        if val >= int(rang[1]):
            token = []
            for i in range(rang[0], rang[1]):
                token.append(None)
            total += len(token) * rang[-1]
        if val < int(rang[1]):
            token = []
            for i in range(rang[0], val):
                token.append(None)
            total += len(token) * rang[-1]
    return total

class win(JFrame):
    def __init__(self, title="Consumo Electrico"):
        JFrame(title)
        self.setLayout(None)
        self.setBounds(10, 10, 300, 180)
        self.show()
        self.build()

    def build(self):
        self.label = JLabel("Cup")
        self.label.setBounds(120, 10, 45, 15)
        self.label2 = JLabel("KWh")
        self.label2.setBounds(20, 10, 45, 15)
        self.label3 = JLabel()
        self.label3.setBounds(120, 30, 55, 15)
        self.textfield = JTextField()
        self.textfield.setBounds(15, 30, 75, 20) 
        self.textfield.addActionListener(lambda x:self.label3.setText(str(calculate(self.textfield.getText()))) )
        button = JButton("Calcular")
        button.setBounds(10, 55, 290, 35)
        button.addActionListener(lambda x: self.label3.setText(str(calculate(self.textfield.getText()))))

        for var in [self.label, self.label2, self.label3, self.textfield, button]:
            self.add(var)
        

#print calculate(100)
o = win()
LAF="com.sun.java.swing.plaf.motif.MotifLookAndFeel"
UIManager.setLookAndFeel(LAF)
SwingUtilities.updateComponentTreeUI(o)
 