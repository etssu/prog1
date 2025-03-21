import turtle
#ULOHA 1.1
'''
def test_parity(n):
    if n%2 ==0:
        return True
    else:
        return False
    
print(test_parity(91))
'''

#ULOHA 1.2
'''
def minimum_dvoch(a,b):
    if a <b:
        return a
    else:
        return b
    
print(minimum_dvoch(843,123))
'''

#ULOHA 1.3
'''
def minimum_troch(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= c and b<=a:
        return b
    else:
        return c
    
print(minimum_troch(-105,-105,1))
'''

#ULOHA 1.4
'''
def menu():
    vstup = input('ur input is: ')
    if vstup == "s":
        for _ in range(4):
            turtle.fd(100)
            turtle.lt(90)
    elif vstup =='t':
        for _ in range(3):
            turtle.fd(100)
            turtle.lt(120)
    else:
        print("Zadali ste neplatný vstup")

menu()
turtle.exitonclick()
'''

#ULOHA 1.5
'''
def pocet_rovnakych(a,b,c):
    if a == b and b == c:
        return 3
    elif a == b or b == c or a == c: 
        return 2
    else: 
        return 0
    
print(pocet_rovnakych(1,2,1))
'''

#ULOHA 1.6
'''
def pocet_delitelnych_5(n):
    pocitadlo = 0
    if n < 0:
        print('argument musi byt nezaporny')
        return -1
    elif n > 0:
        for i in range(n): 
            a = int(input('cislo: '))
            if a % 5 == 0:
                pocitadlo = pocitadlo +1
        return pocitadlo

print(pocet_delitelnych_5(-3))
'''

#ULOHA 1.7
'''
def pocet_delitelnych(n,k):
    pocitadlo = 0
    if n < 0 or k<=0:
        if n<0 and k< 0:
            print('N a K musia byt kladne cisla')
        elif n<0 and k==0:
            print('N musi byt kladne a K nemoze byt 0')
        elif n<0:
            print('N musi byt kladne cislo')
        elif k<0:
            print('K musi byt kladne cislo')
        elif k ==0:
            print('K nemoze byt 0')
        return -1
    elif n > 0 and k>0:
        for _ in range(n):
            a = int(input('cislo n: '))
            if a % k == 0:
                pocitadlo = pocitadlo + 1
        return pocitadlo
        
print(pocet_delitelnych(5,2))
'''
#ULOHA 1.8
'''
def sucet_nacitanych(n):
    sucet = 0
    if n < 0:
        print('N musi byt kladne cislo')
        return -1
    elif n == 0:
        return 0
    elif n > 0:
        for i in range(n):
            a = int(input('cislo: '))
            sucet = sucet + a
        return sucet
    
print(sucet_nacitanych(4))
'''
#uloha 1.9
'''
def minimum(n):
    minimum = input('cislo: ')
    if n < 0 or n==0:
        print('N musi byt kladne cislo')
        return None
    elif n >0: 
        for i in range(n-1):
            nacitane_cislo = input('cislo: ')
            if nacitane_cislo < minimum:
                minimum = nacitane_cislo
        return minimum
    
print(minimum(4))
'''

#uloha 1.10
'''
def druhe_najvacsie(n):
    if n < 2:
        print('Hodnota musi byt aspon 2')
        return None
    elif n >= 2:
        max1 = float('-inf')
        max2 = float('-inf')
        for _ in range(n - 2):
            num = int(input('cislo: '))
            if num > max2:
                max2 = max1
                max1 = num
            elif num > max2 and num != max1:
                max2 = num

        if max2 == float('-inf'):
            return None

        return max2

print(druhe_najvacsie(5))
'''

#uloha 11
'''
def delitelnost(a,b):
    if a % b ==0:
        return True
    else: 
        return False

def je_prvocislo(a):
    if a<2:
        print('cant be')
    elif a > 2:
        for b in range(2, a):
            if delitelnost(a,b):
                return False        #Ak b deli a, tak cislo uz nie je prvocislo
            else: 
                return True

print(je_prvocislo(22))
'''

#uloha 13
'''
def pohyb_veze(x1,y1,x2,y2):
    if x1 == x2 and y1>=1 and y1<=8 and  y2>=1 and y2<=8:
        return True
    elif x1<=8 and x1>=1 and x2<=8 and x2>=1 and y1==y2:
        return True
    else:
        return False
    
print(pohyb_veze(4,4,2,4))
'''
#uloha 14
'''
def rovnaka_farba(x1,y1,x2,y2):
    if x1 >=1 and x1 <= 8 and y1 >=1 and y1 <= 8 and x2 >=1 and x2 <= 8 and y2 >=1 and y2 <= 8:
        if (x1+y1) % 2 == 0 and (x2+y2) % 2 ==0:
            return 'Black', True
        elif (x1+y1) % 2 == 1 and (x2+y2) % 2 ==1:
            return 'White', True
        else:
            return False
print(rovnaka_farba(2,3,3,2))
'''
#uloha 15
'''
def pohyb_krala(x1,y1,x2,y2):
    if abs(x1-x2) and abs(y1-y2) <=1:
        return True
    else: 
        return False
    
print(pohyb_krala(4,4,5,4))
'''

#uloha 16
'''
def pohyb_strelca(x1,x2,y1,y2):
    if x1 >= 1 and x1 <=8 and x2 >= 1 and x2 <=8 and y1 >= 1 and y1 <=8 and y2 >=1 and y2<=8:
        if (x1+x2)%2 == (y1+y2)%2:
            return True
        else:
            return False
    else:
        return False
    
print(pohyb_strelca(1,1,2,2))
'''

#uloha 17
'''
def pohyb_damy(x1,y1,x2,y2):
    if x1 >= 1 and x1 <=8 and x2 >= 1 and x2 <=8 and y1 >= 1 and y1 <=8 and y2 >=1 and y2<=8:
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        if x1 == x2 and y1>=1 and y1<=8 and  y2>=1 and y2<=8:
            return True
        elif x1<=8 and x1>=1 and x2<=8 and x2>=1 and y1==y2:
            return True
        else:
            return False
        
print(pohyb_damy(7,6,5,2))
'''
# uloha 18
def  pohyb_jazdca(x1,y1,x2,y2):
    if x1 and x2 and y1 and y2 <1 or x1 and x2 and y1 and y2 > 8:
        print('na-ah')
    else:
        if abs(x1-x2) == 2 and abs(y1-y2)== 1 or abs(x1-x2) == 1 and abs(y1-y2) == 2:
            return True
        else: 
            return False

print(pohyb_jazdca(5,1,4,3))