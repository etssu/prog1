'''
ULOHA 1
strana_a = 5
obvod = 4*strana_a
obsah = strana_a**2
print(obvod)
print(obsah)

ULOHA 2
strana_a = 3
strana_b = 8
obvod = 2*(strana_a + strana_b)
obsah = strana_a*strana_b

ULOHA 3
sekundy = 10000

hodiny = sekundy // 3600
minuty = (sekundy - hodiny*3600) // 60
sekund = sekundy - hodiny*3600 - minuty*60

print(hodiny)
print(minuty)
print(sekund)

ULOHA 4
kilometre = 8.5
minuty = 25
sekundy = 37

 #V=S/t
hodiny = (minuty * 60 + sekundy)/3600
rychlost = kilometre / hodiny

print(rychlost)
'''

import turtle
'''
for i in range(4):
    turtle.forward(100)
    turtle.left(90)


for i in range(5):
    turtle.forward(100)
    turtle.left(73)


for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

ULOHA C1
for i in range(4):
    for i in range(5):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
'''
'''
# ULOHA C3
for i in range(10):
    for i in range(5):
        turtle.forward(50)
        turtle.left(72)
    turtle.left(36)
    
'''
# ULOHA 2
'''
def nuholnik(n):
    if n ==3:
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)

    elif n == 4:
        for i in range(4):
            turtle.forward(100)
            turtle.left(90)

    elif n == 7:
        for i in range(7):
            turtle.forward(100)
            turtle.left(52)
    else: 
        print('not defined')

nuholnik(7)
'''
#ULOHA 4
'''
step = 100
turtle.fd(step)
for i in range(5):
    turtle.lt(90)
    turtle.fd(step)
    d = turtle.distance(0, 0)
    a = turtle.towards(0, 0)
    turtle.setheading(a)
    turtle.forward(d)
    turtle.setheading(a + 180)
    turtle.forward(d)
turtle.lt(90)
turtle.fd(step)
'''