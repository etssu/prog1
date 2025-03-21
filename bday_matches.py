from random import randint

def duplicate(t):           #t = list
    copy = t[:]             #if there is a collision, return True
    copy.sort()

    for i in range(len(copy)-1):
        if copy[i] == copy[i+1]:
            return True
    return False


def random_date(n):
    bdays = []
    for i in range(n):
        date = randint(1,365)
        bdays.append(date)
    return bdays

def count_matches(ppl, groups):
    count = 0
    for i in range(groups):
        bdays = random_date(ppl)
        if duplicate(bdays):
            count +=1
    return count

def main():
    ppl = int(input('how many ppl: '))
    groups = int(input('how many groups: '))
    count = count_matches(ppl, groups)

    print('there are ', count, ' bdays on the same day')

main()
