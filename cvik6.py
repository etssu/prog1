import math

#uloha 1 
'''
def sucet_kladnych():
    cislo = int(input('cislo: '))
    sum = cislo
    while cislo > 0:
        cislo = int(input('cislo: '))
        if cislo <= 0:
            break
        sum += cislo
    return sum
    
print(sucet_kladnych())
'''

#uloha 2
'''
def stvorce_mensie_n(n):
    i = 1
    while i ** 2 < n:
        print(i**2)
        i += 1

print(stvorce_mensie_n(20))
'''

#uloha 3
'''
def feikovy_logaritus(n):
    x = 0
    power = 1
    while power * 2 <n:
        power *= 2
        x+=1 

    return x

print(feikovy_logaritus(20))
'''
#uloha 4
'''
def index_najvacsieho():
    maximum = None
    max_index = 0
    index = 0
    while True:
        cislo = int(input('cislo: '))
        if cislo == 0:
            break
        elif maximum is None or cislo > maximum:
            maximum = cislo
            max_index = index
        index += 1
    return max_index

print(index_najvacsieho())
'''

#uloha 5
'''
def vacsi_naslednik():
    count = 0
    previous_num = None
    while True:
        cislo = int(input('cislo: '))
        if cislo == 0:
            break
        elif previous_num is not None and cislo > previous_num:
            count += 1
        previous_num = cislo
        if 0 > previous_num:
            count += 1
        previous_num = cislo
    return count

print(vacsi_naslednik())
'''
#uloha 6
'''
def pocet_maxim():
    max_value = None
    count = 0

    while True:
        num = int(input('cislo: '))
        if num == 0:
            break
        if max_value is None or num > max_value:
            max_value = num
            count = 1
        elif num == max_value:
            count += 1
    return count
    
print(pocet_maxim())
'''

#uloha 7
'''
def najdlhsia_postupnost():
    previous_num = None
    count = 0
    dlzka = 0

    while True:
        num = int(input('num: '))
        if num == 0:
            count = 1
            break
        if previous_num is None or num == previous_num:
            previous_num = num
            count +=1 
        elif previous_num is None or num != previous_num:
            if count > dlzka:
                dlzka = count
            previous_num = num
            count = 1
    return dlzka

print(najdlhsia_postupnost())
'''

#uloha 8
'''
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: #ak n >= 2
        predposledny = 1
        posledny = 1
        aktualny = predposledny + posledny
        for i in range(n-2):
            predposledny = posledny
            posledny = aktualny 
            aktualny = predposledny + posledny
        return aktualny

def fibonacci_index(x):
    index = 0
    if x == 1:
        return 0
    while True:
        if fibonacci(x) == x:
            return x
        if fibonacci(x) > x:
            return -1
        index += 1


print(fibonacci_index(8))
'''
#uloha 9
'''
def odhad_pi(epsilon):
    sum_value = 0
    k = 0
    koef = (2* math.sqrt(2))/9801
    while True:
        nominator = math.factorial(4*k) *(1103 + 26390*k)
        denominator = ((math.factorial(k))**4) * 396**(4*k)
        term = koef * (nominator/denominator)
        sum_value += term

        if abs(term) < epsilon:
            break

        k += 1
    odhad_pi = 1 / sum_value
    return odhad_pi

print(odhad_pi(1000))
'''
#uloha 10
'''
def kvocient(a,b):
    times  = 0
    if b == 0:
        return None
    while a >= b:
        a-=b
        times +=1 
        if a == 0:
            break
    return times

print(kvocient(15, 2))
'''
#uloha 11
'''
def modulo(a,b):
    times = 0
    if b == 0:
        return None
    if a < b:
        return a
    while a >= b:
        a-=b
        times += 1
        if a < b:
            return a

print(modulo(1, 4))
'''
#uloha 12
def factorizacia(n):
    dilnuk = 2
    while n > 1:
        while n % dilnuk == 0:
            print(dilnuk)
            n //= dilnuk
        dilnuk += 1

factorizacia(37)
        


        
    