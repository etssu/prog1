import bisect
def in_bisect(zoznam_slov, slovo):
    if len(zoznam_slov) == 0:
        return False
    
    i = len(zoznam_slov) // 2
    if zoznam_slov[i] == slovo:
        return True
    
    if zoznam_slov[i] < slovo:
        return in_bisect(zoznam_slov[i+1:], slovo)
    else:
        return in_bisect(zoznam_slov[:i], slovo)
    

def najdi_reverzny_par():
    word_list = []
    with open('words.txt') as file:
        for line in file:
            word = line.strip()
            word_list.append(word)
    for word in word_list:
        reverse = word[::-1]
        if in_bisect(word_list, reverse) and word != reverse:
            print(f'pair: {word}, {reverse}')


#najdi_reverzny_par()
def is_interlock(word_list, il_word):
    return (in_bisect(word_list, il_word[::2]) and in_bisect(word_list, il_word[1::2]))

def najdi_prepletene_slova():
    word_list = []
    with open('words.txt') as file:
        for line in file:
            word = line.strip()
            word_list.append(word)
    print('prepletene: ')
    for word in word_list:
        if is_interlock(word_list, word):
            print(f' {word} je interlock  {word[::2]} a {word[1::2]}')

najdi_prepletene_slova()

