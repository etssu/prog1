import copy
import time

def najviac_nacitane():
    zoznam = []
    uni_zoznam = []
    pocet = 0
    number = int(input('num: '))
    while number != 0:
        number = int(input('num: '))
        zoznam.append(number)
        if number == 0:
            break
    
    index = 0
    for index in range(len(zoznam)-1):
        if zoznam[index] > pocet:
            pocet = zoznam[index]
    return pocet

#print(najviac_nacitane())


def stred(t):
    if t == []:
        print('chyba: zoznam je prazdny :(')
        return None
    else: 
       t2 = copy.deepcopy(t)
       t2= t2[1:-1]
       return t2
#print(stred([5, [], 'a', [1,2,3], -5.5]))
#print(stred([]))

def vyrez(t):
    if t == []:
        print('chyba: zoznam je prazdny')
        return None
    else:
        del t[0]
        del t[-1]
        return None

#print(vyrez([5, [], 'a', [1,2,3], -5.5]))
#print(vyrez([]))

def sucet_matic(A, B):
    if len(A) != len(B):
        print('Zadane matice nie je mozne scitat')
        return None
    else:
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(A[i])):
                row.append(A[i][j]+B[i][j])
            result.append(row)
        return result

#print(sucet_matic([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]]))

def sucin_matic(A,B):
    if len(A[0]) != len(B):
        print('Zadane matice nie je mozne vynasobit')
        return None
    else:
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                suma = 0
                for k in range(len(B)):
                    suma += A[i][k]*B[k][j]
                row.append(suma)
            result.append(row)
        return result
#print(sucin_matic([[1,2],[3,5],[-2,-1]], [[2],[-2]]))

def spolocny_prienik(intervaly):
    intervaly.sort()
    for i in range(len(intervaly)-1):
        for j in range(i+1, len(intervaly)):
            if intervaly[i][1] <= intervaly[j][0]:
                return False
    return True
#print(spolocny_prienik([[0,4],[2,5],[4,7]]))

def ma_duplikat(t):
    duplikaty = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] == t[j]:
                cislo = t.count(i)
                duplikaty.append(cislo)
    return len(duplikaty) > 0
#print(ma_duplikat([ 'a', 1, 4, 5,]))

def porovnavanie():
    def vytvor_zoznam_slov_append():
        zoznam = []
        fin = open('words.txt')
        for line in fin:
            word = line.strip()
            zoznam.append(word)
        return zoznam

    def vytvor_zoznam_slov_plus():
        zoznam = []
        file = open('words.txt')
        for line in file:
            word = line.strip()
            zoznam += [word]
        return zoznam


    start_time = time.time()
    t = vytvor_zoznam_slov_append()
    end_time = time.time() - start_time

    print(len(t))
    print(t[:10])
    print(end_time, 'seconds')

    starts_time = time.time()
    t = vytvor_zoznam_slov_plus()
    ends_time = time.time() - starts_time
    print(len(t))
    print(t[:10])
    print(ends_time, 'seconds')

def delitelnost(a,b):
    return a % b == 0

def je_prvocislo(a):
    if a<2:
        print('cant be')
    elif a > 2:
        for b in range(2, a):
            if delitelnost(a,b):
                return False        #Ak b deli a, tak cislo uz nie je prvocislo
            else: 
                return True

def rozloz_na_prvocisla(t):
    vysledok = []
    for prvok in t:
        aktualne_cislo = prvok
        while aktualne_cislo > 1:
            for i in range(2, aktualne_cislo+1):
                if je_prvocislo(i):
                    if aktualne_cislo % i == 0:
                        vysledok.append(i)
                        aktualne_cislo = aktualne_cislo // i
                        break
            if aktualne_cislo == 1:
                break
        vysledok.append(0)
    return vysledok

print(rozloz_na_prvocisla([14, 11, 18]))


                            
