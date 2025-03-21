#uloha 1
def pocet_vyskytov(retazec, podretazec):
    pocet = retazec.count(podretazec)
    return pocet

#print(pocet_vyskytov('banana', 'a'))

#uloha 2
def je_palindrom(ret):
    if ret[::-1] == ret[0:]:
        return True
    else:
        return False
    
#print(je_palindrom('annA'))

#uloha 3
def je_palindrom(ret):
    if len(ret) <= 1:
        return True
    else: 
        if ret[0] != ret[-1]:
            return False
        else:
            return je_palindrom(ret[1:-1])
    
#print(je_palindrom('ana'))

#uloha 4

def any_lowercase(s):
    for c in s:
        if 'c'.islower():
            return True
        else:
            return False
        
#print(any_lowercase('Anna'))

def cezar(OT, posun):
    novy_retazec = ''
    for znak in OT:
        if 'A' <= znak <= 'Z': 
            novy_znak = chr((ord(znak)- ord('A')+ posun)%26 + ord('A'))
        else:
            novy_znak = znak
        novy_retazec += novy_znak
    print(novy_retazec)

#cezar('WHY', 7)

fin = open('words.txt')
for riadok in fin:
    slovo = riadok.strip()

def slova_dlhsie_nez(n):
    fin = open('words.txt')
    for riadok in fin:
        slovo = riadok.strip()
        if len(slovo) >=n:
            print(slovo)

#slova_dlhsie_nez(21)

def neobsahuje_e1(slovo):
    if not 'e' in slovo: 
        return True
    else:
        return False
#print(neobsahuje_e1('abeceda'))

def neobsahuje_e2():
    fin = open('words.txt')
    count = 0
    for riadok in fin:
        slovo = riadok.strip()  
        if not 'e' in slovo:
            print(slovo)
            count += 1
    percent = (count*100)/113783
    print(percent)

#neobsahuje_e2()

def neobsahuje(slovo,pismena):
    for pismeno in pismena:
        if pismeno in slovo:
            return False
    else:
        return True

#print(neobsahuje("programovanie", "xyz"))

def pouziva_len(slovo,pismena):
    for pismeno in slovo:
        if pismeno not in pismena:
            return False
    else:
        return True
    
#print(pouziva_len('stlp','prstl'))

def pouziva_vsetky(slovo,pismena):
    for pismeno in pismena:
        if pismeno not in slovo:
            return False
    else:
        return True
    
#print(pouziva_vsetky('abeciedka','abcdef'))

def je_vzostupne(slovo):
    for znak in range (len(slovo)-1):
        if slovo[znak] > slovo[znak+1]:
            return False
    else: return True

#print(je_vzostupne('abeceda'))

def tri_dvojite(ret):
    count = 0
    i = 0
    while i < len(ret)- 1:
        if ret[i] == ret[i+ 1]:
            count += 1
            i += 2
        else: 
            i+=1 
        if count == 3:
            return True
    return False 

#print(tri_dvojite('commttee'))

def tri_dvojit():
    with open('words.txt') as file:
        for riadok in file:
            ret = riadok.strip()
            if tri_dvojite(ret):
                print(ret)

#print(tri_dvojit())

def zrkadlovy_vek(vek):
    int(str(vek)[::-1])

pocet = 0

for dcera in range(10,100):
    mama = zrkadlovy_vek(dcera)
    if mama is not None:
        rozdiel = mama - dcera
        if mama > dcera and rozdiel >= 18:
            pocet += 1
            if pocet == 6:
                print(dcera)

