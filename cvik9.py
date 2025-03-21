def nested_sum(zoznam_zoznamov_cisel):
    suma = 0
    for zoznam in zoznam_zoznamov_cisel:
        for cislo in zoznam:
            suma += cislo
    return suma

#print(nested_sum([[5,-1],[0],[1,10,7,9],[-4]]))

#uloha2
def cumsum(zoznam_cisiel):
    zoznam = []
    sucet = 0
    for cislo in zoznam_cisiel:
        sucet += cislo
        zoznam.append(sucet)
    return zoznam

#print(cumsum([2,4,8]))

#uloha 3
def je_zoradeny(zoznam_cisel):
    for index in range(len(zoznam_cisel)-1):
        if zoznam_cisel[index] > zoznam_cisel[index+1]:
            return False
    return True

#print(je_zoradeny([1,2,2,3]))

#uloha 4
def sucet_parnych_pozicii(zoznam_cisel):
    suma = 0
    index = 0
    for cislo in zoznam_cisel:
        if index % 2 == 0:
            suma += cislo
            index += 1
        else:
            suma = suma
            index +=1
    return suma

#print(sucet_parnych_pozicii([2, 5, 3, -2, -3, 0, 1]))

#uloha 5
def pocet_lokalnych_maxim(zoznam_cisel):
    pocet = 0
    for index in range(1, len(zoznam_cisel)-1):
        if zoznam_cisel[index] > zoznam_cisel[index+1] and zoznam_cisel[index] > zoznam_cisel[index-1]:
            pocet +=1
    return pocet 
#print(pocet_lokalnych_maxim([2, 5, 3, -2, -3, 0, -1]))

def pocet_roznych(zoznam):
    uni = []
    for element in zoznam:
        if element not in uni:
            uni.append(element)   
    return len(uni)

#print(pocet_roznych([2, 'a', [1,2], 'a', [1,2], 3]))

def pocet_unikatnych(zoznam):
    pocet = 0
    for element in zoznam:
        if zoznam.count(element) == 1:
            pocet +=1
    return pocet

#print(pocet_unikatnych([2, 'a', [1,2], 'a', [1,2], 3]))

def je_anagram(retazec1, retazec2):
    if len(retazec1) != len(retazec2):
        return False
    pismena1 = list(retazec1)
    pismena2 = list(retazec2)
    pismena1.sort()
    pismena2.sort()
    return pismena2 == pismena1

print(je_anagram('skola','laska'))