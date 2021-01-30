import os

val = int(input("Ingrese su consumo en KWh: "))

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

print("Lamentablemente debera pagar %.2f cup..." % (total))
