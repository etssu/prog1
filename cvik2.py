#ULOHA 1.1
'''
def tretia_mocnina(a):
    print(a*a*a)

tretia_mocnina(3)
'''
#ULOHA 1.2
'''
def tretia_mocnina(a):
    return(a*a*a)

navratova_hodnota = tretia_mocnina(2)
print("Funkcia vratila hodnotu:", navratova_hodnota)
'''
#ULOHA 1.3
"""
def priemer_troch(a,b,c):
    print((a+b+c)/3)

priemer_troch(1,2,3)
"""

#ULOHA 1.4
"""
def priemer_troch(a,b,c):
    return((a+b+c)/3)

navratova_hodnota = priemer_troch(1,2,3)
print('Navratova hodnota je:', navratova_hodnota)
"""
#ULOHA 2.1
'''
def vypis(n):
    for i in range(n):
        print(i+1)
vypis(10)
'''
#ULOHA 2.2
'''
def vypis(n):
    for i in range(n):
        print(i+101)
vypis(3)
'''
#ULOHA 2.3
'''
def vypis(n):
    for i in range(n):
        print((i+1)*2)
vypis(5)
'''
#ULOHA 2.4
'''
def vypis(n):
    for i in range(n):
        print(n-i)
vypis(5)
'''
#ULOHA 2.1(R)
'''
def vypis(n):
    for i in range(1, 11):
        print(i)
vypis(10)
'''
#ULOHA 2.2(R)
'''
def vypis(n):
    for i in range(101, n+101):
        print(i)
vypis(3)
'''

#ULOHA 2.3(R)
'''
def vypis(n):
    for i in range(2, 2+(2*n), 2):
        print(i)
vypis(10)
'''

#ULOHA 2.4(R)
'''
def vypis(n):
    for i in range(n, 0, -1):
        print(i)
vypis(5)
'''

#ULOHA 2.5
'''
def sucet_stvorcov(n):
    sucet = 0
    k = 2
    for i in range(1, n+1):
        sucet = sucet + (i**k)
    return (sucet)
    
sucet_stvorcov = sucet_stvorcov(5)
print(sucet_stvorcov)
'''


#ULOHA 2.6
#an = a0 + d(n-1)
'''
def aritmeticka_postupnost(a0, d, N):
    for i in range(N):
        print(a0 + i*d)

aritmeticka_postupnost(5, -3, 4)
'''
#ULOHA 2.7
'''
def geometricka_postupnost(a0,q,N):
    for i in range(N):
        print(a0*(q**i))

geometricka_postupnost(1,2,5)
'''

#ULOHA 2.8
'''
def postupny_sucet_geometrickeho_radu(a0,q,N):
    print("Prvy clen je:", a0)
    print(int(a0*(1-q**2)/(1-q)))
    for i in range(N+1):
        print(int(a0*(1-q**i)/(1-q)))

postupny_sucet_geometrickeho_radu(1,2,5)
'''
#ULOHA 2.9
'''
def grid(n):
    for i in range(n):
        print('+----' * n +'+')
        print('|    ' * n + '|')
        print('|    ' * n + '|')
    print('+----'*n +'+')

grid(3)
'''
#ULOHA 10
'''
def vynasob(a,b):
    result = 0
    for _ in range(b):
        result +=a 
    return result       

#ULOHA 11

def tretia_mocnina(a):
    b = 3
    vynasob(a,b)

print(tretia_mocnina(3))
'''

#ULOHA 14
'''
def od_1_po_n(n):
    for i in range(1,n+1):
        for i in range(1,i+1):
            print(i, end=' ')
        print()

od_1_po_n(5)
'''

#ULOHA 13
'''
def mala_nasobilka():
    print('        ', end='')
    for i in range(1, 11):
        print(f"{i:4}", end='\t')
    print()
    for i in range(1,11):
        print(f"{i:2} ", end="\t")
        for n in range(1,11):
            print(f"{i*n:4}", end="\t")
        print()
mala_nasobilka()
'''
