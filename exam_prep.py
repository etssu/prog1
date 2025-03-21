#SKUP A
def F(x):
    sucet = 0
    while True:
        cislo = int(input('cislo: '))
        sucet += cislo
        if sucet > x:
            break
    return sucet
#print(F(100))

def F(t):
    for i in range(len(t)):
        if i % 2 ==0:
            t[i] = 0

def F(ret1):
    count = 0
    for letter in ret1:
        if letter.isupper():
            count += 1
    return count

#print(F('bAnanA'))

def F(n):
    if n == 0:
        return ''
    else:
        retazec = input('slovo: ')
    return retazec[0] + F(n-1)

#print(F(5))

def F(n):
    count = 0
    if n < 3:
        return 0
    num1 = int(input('cislo: '))
    current = int(input('cislo: '))

    for i in range(n-2):
        next_num = int(input('cislo: '))
        if current > num1 and current > next_num:
            count += 1
    return count

#print(F(5))
        #riadki
def F(A):
    for i in A:
        sucet = sum(i)
        print(sucet)
#F([[1,2,3],[4,5,6],[7,8,9]])

#stlpce
def F(a):
    sums = []
    count = 0
    for col in range(len(a[0])):
        sucet = 0
        for row in range(len(a)):
            sucet += a[row][col]
        sums.append(sucet)
    
    unique_sums = set()
    for j in sums:              #j is one sum from the list
        if j in unique_sums:
            count += 1
            if count >= 1:
                return True
        unique_sums.add(j)
    return False

#print(F([[0, 1, 0],[0, 0, 0],[0, 0, 3]]))


#SKUP B
def f1():
    zoznam = []
    while True:
        num = int(input('cislo: '))
        if num not in zoznam:
            zoznam.append(num)
        else: return num

#print(f1())

def f2(t, x):
    for i in range(len(t)):
        if t[i] < x:
            del t[i]
            t.insert(i, 0)
    
#f2([11,22,33,44], 32)

def f3(n):
    zoznam = []
    if n == 0:
        return zoznam
    else:
        zoznam = f3(n-1)
        num = int(input('cislo: '))
        if num % 2 == 0:
            zoznam.append(num)
    return zoznam

#print(f3(5))

def f4(t):
    for word in t:
        if word[0].isupper():
            return word

#f4(['haA','aHa', 'Haha'])
        

def f5(A):
    for col in range(len(A[0])):
        if all(row[col]== A[0][col] for row in A):
            return True
    return False

#print(f5([[1,3,3], [3,2,5], [7,2,10]]))


def f6(n):
    pocet_r = 0
    same = 0
    num = int(input('num: '))
    for _ in range(n):
        num2 = int(input('num: '))
        if num == num2:
            same += 1
            print(same)
            if same >= 2:
                pocet_r +=1
        if num != num2:
            same = 1
    return pocet_r

#print(f6(7))


#1.1
def F(a,b,c,d):
    if a >= c and b <= d or c >= a and d <= b:
        return True
    return False
#print(F(1,2,3,4))

#1.2
def F1(a,b,c,d):
    if b <= c or d <= a:
        return False
    return True
#print(F1(1,6,1,4))
#1.3
def F3(a,b,x):
    if abs(x-a) < abs(x-b):
        return a
    else: return b
#print(F3(1,100,49))
#2.1
def r(ret1, ret2):
    for pismeno in ret1:
        if pismeno in ret2:
            return True
    return False
#print(r('banana', 'rgessive'))
#2.2
def r2(ret1, ret2):
    for pismeno in ret1:
        if pismeno not in ret2:
            return False
    return True
#print(r2('banana', 'blin'))
#2.3
def r31(ret):
    unique = []
    for pismeno in ret:
        if pismeno in unique:
            return True
        unique.append(pismeno)
    return False

def r32(ret):
    return len(set(ret)) != len(ret)
#print(r32('bana'))

def r41(ret):
    return max(ret)
#print(r41('otec'))
def r42(ret):
    maximalne = ret[0]
    for pismeno in ret:
        if pismeno > maximalne:
            maximalne = pismeno
    return maximalne
#print(r42('otec'))

#3.1
def rek1(n):
    if n == 1:
        ret = input('ret: ')
        return ret
    else:
        ret = input('ret: ')
        maximalne = rek1(n-1)
        if len(ret) >= len(maximalne):
            maximalne = ret
        return maximalne  
#print(rek1(3))

def rek2(ret):
    if len(ret) == 0:
        return 0
    if ret[0].isupper():
        return 1 + rek2(ret[1:])
    else:
        return rek2(ret[1:])
#print(rek2('AnNa'))

#3.3
def rek3(ret,x):
    if len(ret) == 0:
        return False
    if ret[0] == x:
        return True
    else:
        return rek3(ret[1:],x)

#print(rek3('banana','m')) 
#3.4
def rek4(ret,x):
    if len(ret) == 0:
        return 0
    if ret[0] == x:
        return 1 + rek4(ret[1:],x)
    else:
        return rek4(ret[1:], x)
#print(rek4('banana', 'n'))

#3.5
def rek5(n):
    if n == 0:
        return 0
    if n > 0:
        retazec = input('retazec: ')
        if len(retazec) > 5:
            return 1 + rek5(n-1)
        return rek5(n-1)
#print(rek5(5))

#3.6
def rek6(n):
    if n == 1:
        return 1
    else:
        return ((-1) ** (n+1)) * n + rek6(n-1)

#print(rek6(5))

def rek7(ret):
    if len(ret) <= 1:
        return True
    if ret[0] != ret[-1]:
        return False
    else:
        return rek7(ret[1:-1])
#print(rek7('banab'))

#4.1
def w(k):
    pocet = 1
    pred_cislo = int(input('cislo: '))
    while pocet < k:
        cislo = int(input('cislo: '))
        if cislo == pred_cislo:
            pocet += 1
        else: 
            pocet = 1
        pred_cislo = cislo
    return pred_cislo
#print(w(3))

#4.2
def w2():
    pocet_rovin = 0
    count = 1
    rovina = False
    pred_cislo = int(input('cislo: '))
    while True:
        cislo = int(input('cislo: '))
        if cislo == 0:
            break
        if cislo == pred_cislo:
            count += 1
            if count >= 2 and not rovina:
                pocet_rovin += 1
                rovina = True
        else:
            count = 1
            rovina = False
        pred_cislo = cislo
    return pocet_rovin
#print(w2())

#4.3
def w3():
    pocet = 0
    pred_cislo = int(input('cislo: '))
    cislo = int(input('cislo: '))
    while True:
        nasled_cislo = int(input('cislo: '))
        if nasled_cislo > pred_cislo + cislo:
            pocet += 1
        if nasled_cislo == 0:
            break
        pred_cislo = cislo
        cislo = nasled_cislo
    return pocet
#print(w3())

def w4():
    pocet_maxim = 0
    pred_cislo = int(input('cislo: '))
    cislo = int(input('cislo: '))
    while True:
        nasled_cislo = int(input('cislo: '))
        if cislo > pred_cislo and cislo > nasled_cislo:
            pocet_maxim += 1
        if nasled_cislo == 0:
            break
        pred_cislo = cislo
        cislo = nasled_cislo
    return pocet_maxim
#print(w4())

def w5():
    retazec1 = input('ret: ')
    pocet_ret = 1
    while True:
        retazec2 = input('ret: ')
        if retazec1[0] == retazec2[0]:
            pocet_ret += 1
            break
        else:
            pocet_ret += 1
        retazec1 = retazec2
    return pocet_ret
#print(w5())

#5.1
def F(t):
    for element in t:
        for letter in element:
            if letter == 'a':
                return element
    return None
#print(F(['otaec','xer','banan','mama']))

#5.2
def F(t):
    new_word = ''
    for element in t:
        new_word += element[0]
    return new_word
#print(F(['mama','otec']))

#5.3
def F(t):
    pocet = 0
    for element in t:
        unique_l= []
        unique = True
        for letter in element:
            if letter in unique_l:
                unique = False
                break
            unique_l.append(letter)
        if unique:
            pocet +=1
    return pocet
#print(F(['otec', 'mama', 'kon', 'gola']))
#5.4
def F(t):
    pocet_max = 0
    max_ret = ''
    for ret in t:
        pocet_znakov = len(set(ret))
        if pocet_znakov > pocet_max:
            pocet_max = pocet_znakov
            max_ret = ret
    return max_ret
#6.1
def F(n):
    t = []
    sucet = 0
    while True:
        cislo = int(input('cislo: '))
        sucet += cislo
        t.append(cislo)
        if sucet > n:
            return t
 #6.2
def F(n):
    t = []
    while True:
        cislo = int(input('cislo: '))
        if cislo in t:
            break
        t.append(cislo)
    return t
#print(F(5))
        
#6.3
def F(n):
    t = []
    while True:
        cislo = int(input('cislo: '))
        t.append(cislo)
        if len(t) > 1 and (max(t)-min(t)) > n:
            break
    return t
#print(F(10))

#6.4
def F(n):
    t = []
    unique_nums = set()
    while len(unique_nums)<n:
        cislo = int(input('cislo: '))
        t.append(cislo)
        unique_nums.add(cislo)
    return t
#print(F(3))

#7.1
def F(A,x):
    for riadok in A:
        if x in riadok:
            return True
    return False
#print(F([[1,2,3],[4,5,6],[7,8,9]], 5))
        
#7.2
def F(A,x):
    count = 0
    for riadok in A:
        if x in riadok:
            count += 1
    return count
#print(F([[1,5,3],[4,5,6],[7,8,5]], 5))

#7.3
def F(A):
    maximum = A[0][0]
    for riadok  in A:
        for cislo in riadok:
            if cislo > maximum:
                maximum = cislo
    return maximum        
#print(F([[1,5,3],[4,5,6],[7,8,5]]))

#7.4
def F(A):
    maximum = A[0][0]
    max_i, max_j = 0,0
    for i in range(len(A)):                             #riadok
        for j in range(len(A[0])):                      #stlpec
            if A[i][j] > maximum:
                maximum = A[i][j]
                max_i = i
                max_j = j
    return max_i, max_j

#print(F([[10,5,3],[4,5,6],[7,80,11]]))
 #7.5
def F(A):
    pocet = 0
    for j in range(len(A[0])): #stlpec
        all_zero = True
        for i in range(len(A)): #riadok
            if A[i][j] != 0:
                all_zero = False
                break
        if all_zero == True:
            pocet +=1 
    return pocet

#print(F([[0,0,2], [0,0,0],[0,0,2]]))
#7.7
def F(A):
    for j in range(len(A[0])):
        rovnake = True
        seen = []
        
        for row in A:
            if row[j] in seen:
                rovnake = False
                break
            seen.append(row[j])
        if rovnake:
            return True
    return False
#print(F([[0,0,3], [0,0,1],[0,0,2]])) 
#7.6

def F(A):
    for j in range(len(A[0])): #stlpce
        rovnake = True
        for i in range(1,len(A)):
            if A[i][j] != A[0][j]:
                rovnake = False
                break
        if rovnake:
            return True
    return False
#print(F([[5,1,3], [0,0,1],[0,0,2]])) 
#7.8
def F(A):
    max_sucet = 0
    max_index = -1
    index = -1
    for j in range(len(A[0])): #stlpec
        sucet = 0
        index += 1
        for i in range(len(A)): #riadok
            sucet += A[i][j]
        if sucet > max_sucet:
            max_sucet = sucet
            max_index = index
    return max_index
#print(F([[8,1,3], [0,0,1],[0,0,2]]))  

#7.9
def F(A):
    sums = []
    for j in range(len(A[0])): #stlpce
        sucet = 0
        for i in range(len(A)): #riadki
            sucet += A[i][j]
        if sucet in sums:
            return True
        sums.append(sucet)
    return False
#print(F([[6,1,3], [0,0,1],[0,0,2]]))    
 #8.1
def F(t,x):
    pocet = 0
    for interval in t:
        if interval[0] <= x <= interval[1]:
                pocet +=1 
    return pocet
#print(F([[1,5],[8,9],[3,7]], 4))

#8.2
def F(t,x):
    for interval in t:
        if interval[0] <= x <= interval[1]:
            return interval
    return None
#print(F([[1,5],[4,5],[2,7]], 6))

#8.3
def F(t,x):
    intervaly = []
    for interval in t:
        if interval[0] <= x <= interval[1]:
            intervaly.append(interval)
    return intervaly
#print(F([[1,5],[4,8],[2,7]], 6))  
# 8.4
def F(t):
    for i in range(len(t)):
        prienik = True
        for j in range(len(t)):
            if i != j:
                interval_1 = t[i]
                interval_2 = t[j]
                if not (interval_1[1] <= interval_2[0] or interval_2[1] <= interval_1[0]):
                    prienik = False 
                    break  
        if prienik:  
            return True  
    return False  
#print(F([[1,2],[4,8],[2,7]]))

