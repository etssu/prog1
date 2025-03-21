import turtle
import math 

#uloha 1 a
'''
def obdlznik():
    for i in range(2):
        turtle.fd(50)
        turtle.lt(90)
        turtle.fd(100)
        turtle.lt(90)

obdlznik()
'''
#uloha 1 b
'''
def obdlznik(a,b):
    for i in range(2):
        turtle.fd(a)
        turtle.lt(90)
        turtle.fd(b)
        turtle.lt(90)

obdlznik(50, 100)
'''
#uloha 1c 
"""
def kosostvorec(a, alfa):
    for i in range(2):
        turtle.fd(a)
        turtle.lt(alfa)
        turtle.fd(a)
        turtle.lt(180-alfa)

kosostvorec(100,60)
"""

#uloha 1d 
'''
def rovnobeznik(a,b,alfa):
    for i in range(2):
        turtle.fd(a)
        turtle.lt(alfa)
        turtle.fd(b)
        turtle.lt(180-alfa)

rovnobeznik(100,200,60)
'''

#uloha 1e
'''
def rovnobeznik(a,b,alfa):
    for i in range(2):
        turtle.fd(a)
        turtle.lt(alfa)
        turtle.fd(b)
        turtle.lt(180-alfa)

def obdlznik(a,b):
    alfa = 90
    rovnobeznik(a,b,alfa)

obdlznik(50,100)

def kosostvorec(a,alfa):
        b = a
        rovnobeznik(a,b,alfa)

kosostvorec(50, 60)
'''

#uloha 2

def utvar(n, strana):
    uhol = 360/n
    uhol2 = ((180-uhol)/2)
    stranab = ((math.sin(math.radians(uhol2))*strana)/math.sin(math.radians(uhol)))
    for i in range(n):
        turtle.fd(stranab)
        turtle.lt(180-uhol2)
        turtle.fd(strana)
        turtle.lt(180-uhol2)
        turtle.fd(stranab)
        turtle.lt(180-uhol)
        turtle.right(uhol) 

utvar(5,100)