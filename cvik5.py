#uloha 1
'''
def sucet_rekurzivne(n):
    if n == 1:
        return 1
    else:
        sucet = 0
        sucet += sucet_rekurzivne(n-1) + n
    return sucet

print(sucet_rekurzivne(6))
'''
#uloha 2
'''
def sucet_rekurzivne(n):
    if n == 0:
        return 0
    else:
        cislo = int(input(': '))
        if cislo % 2 == 0:
            return 1 + sucet_rekurzivne(n-1)
        else:
            return sucet_rekurzivne(n-1)

print(sucet_rekurzivne(5))
'''

#uloha 3
'''
def maximum_rekurzivne(n):
    if n == 1:
        maximum = int(input('cislo: '))
        return maximum
    else:
        akt = maximum_rekurzivne(n-1)
        cislo = int(input('cislo: '))
        if cislo > akt:
            maximum = cislo
        else:
            maximum = akt
        return maximum
   
maximum_2 = maximum_rekurzivne(3)
print(maximum_2)
'''
#uloha 4
'''
def parita_suctu_rekurzivne(n):
    if n == 1:
        cislo =  int(input('cislo: '))
        if cislo%2 == 0:
            return True
        else:
            return False
    else:
        if parita_suctu_rekurzivne(n-1) == True:
            cislo = int(input('cislo: '))
            if cislo % 2 == 0:
                return True
            else:
                return False
        else:
            cislo = int(input('cislo: '))
            if cislo % 2 == 0:
                return False
            else:
                return True
        
print(parita_suctu_rekurzivne(4))
'''

#uloha 5

def sucet_prvocisiel(n):
    def je_prvocislo(num, div =2):
        if num < 2:
            return False
        elif num <= 3:
            return True
        elif num%2 == 0 or num%3 ==0:
            return False
        else:
            return True
    
    if n <= 2:
        return 0
    else:
        if je_prvocislo(n-1) == True:
            return (n-1) + sucet_prvocisiel(n-1)
        else: 
            return sucet_prvocisiel(n-1)
        
print(sucet_prvocisiel(13))


#uloha 2.1
'''
def je_mocnina(a,b):
    if a == b:
        return True
    elif (a % b) != 0 or a <b:
        return False
    return je_mocnina(a // b, b)

print(je_mocnina(9,2))
'''
#uloha 2.2
'''
def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
    
print(GCD(10,20))
'''

#uloha 2.3
'''
def dec_to_bin(n):
    if n == 0:
        print(0, end='')
    elif n > 0:
        dec_to_bin(n//2)
        print(n % 2, end='')

dec_to_bin(10)
'''
#uloha 2.4
'''
def mince(suma,pocet, minca = 0.50):
    if suma == 0 and pocet == 0:
        return True
    elif suma < 0 or pocet <0:
        return False
    else:
        if minca == 0.50:
            return (suma - minca, pocet -1, 0.50) and True or (suma, pocet, 0.20) and True
        if minca == 0.20:
            return (suma - minca, pocet -1, 0.20) and True or (suma, pocet, 0.10) and True
        if minca == 0.10:
            return (suma - minca, pocet - 1, 0.10) or (suma, pocet, 0.5)
        if minca == 0.05:
            return (suma - minca, pocet -1, 0.05) or (suma, pocet, 0.02)
        if minca == 0.02:
            return (suma - minca, pocet -1, 0.02) or (suma, pocet, 0.01)
        if minca == 0.01:
            return (suma - minca, pocet -1, 0.01)
    return False

print(mince(1.00, 2, 0.5))
'''
def move(start, target):
    print('We moved from {} to {}!'.format(start,target))
#def moveVia(start, target):
    #move('A', "B")
    #move("B", "C")

#moveVia('A', "C")

def hanoi_veza(n, start, helper, target):
    if n <= 0:
        return 0
    else:
        hanoi_veza(n-1, start, target, helper)
        move(start, target)
        hanoi_veza(n-1, helper, start, target)

#hanoi_veza(4, 'A', 'B', 'C')
'''
def hanojske_veze_pocet_presunov(n):
    if n == 1:
        return 1
    return 2 * hanojske_veze_pocet_presunov(n-1) + 1

print(hanojske_veze_pocet_presunov(64))

def roky(n):
    print((hanojske_veze_pocet_presunov(64) / 365) + 64/4)

print(roky(1))
'''