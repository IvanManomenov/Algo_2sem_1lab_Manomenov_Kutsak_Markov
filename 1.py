def fibo_write(n):  # запись первых n чисел Фибоначи в массив
    fibo = [0, 1]
    for i in range(n - 2):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo


def union(mass):  # объединение массива чисел в слитную строку
    s = ""
    for i in mass:
        s += str(i)
    return s


def simple(s, sub):  # наивный поиск подстроки
    cnt = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            cnt += 1
    return cnt


def hash(simb, s):  # вычисление хэша строки s в словаре simb
    w = len(simb)
    hsh = sum([simb[s[i]] * (w ** (len(s) - i - 1)) for i in range(len(s))])
    return hsh


def rabin_karp(s, sub):  # алгоритм Рабина-Карпа
    simb = {}
    # составление словаря всех символов, содержащихся в строке
    for i in s:
        if not (i in simb.keys()):
            simb[i] = len(simb.keys())
    for i in sub:
        if not (i in simb.keys()):
            simb[i] = len(simb.keys())
    # print(simb)
    ans_hash = hash(simb, sub)  # хэш искомой подстроки
    # print(ans_hesh)
    cnt = 0
    for i in range(len(s) - len(sub) + 1):
        c_hash = hash(simb, s[i: i + len(sub)])  # хэш текущей подстроки
        if c_hash == ans_hash:
            cnt += 1
    return cnt


def fnd(ch, s):
    for i in range(len(s)):
        if s[len(s) - i - 1] == ch:
            return len(s) - i - 1
    return -1


def boyer_mur(s, sub):  # Алгоритм Бойера-Мура
    l = len(sub)
    i = 0
    cnt = 0
    while i <= len(s) - l:
        flag = 1

        for j in range(l):
            if s[i + l - j - 1] != sub[l - j - 1]:  # если элементы строки и поджстроки не совпадают - сдвигаем итератор
                flag = 0
                k = fnd(s[i + l - j - 1], sub)
                if k == - 1 or k >= l - j - 1:
                    i += len(sub)
                else:
                    i += (l - j - 1) - k
                break
        if flag:
            cnt += 1
            i += 1
    return cnt

def pref(s):  # вычисление префикс-функции строки
    p = [0 for i in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p

def knut_morris_pratt(s, sub):  # алгоритм Кнута-Морриса-Пратта
    st = sub + '#' + s
    p = pref(st)
    #print(st)
    sl = len(s)
    l = len(sub)
    #print(p)
    cnt = 0
    for i in range(sl):
        if p[l + i + 1] == l:
            cnt += 1
    return cnt


fibo = fibo_write(500)
string = union(fibo)
while True:
    try:
        num = int(input(
            "Выберите алгоритм поиска (0 - наивный, 1 - Рабина-Карпа), 2 - Бойера-Мура, 3 - Кнута-Морриса-Пратта "))
        if (num >= 0) and (num < 4):
            break
        print("Некорректный ввод")
    except:
        print("Некорректный ввод")
ms = [0 for i in range(10)]

for i in range(10, 100):
    s = str(i)
    if num == 0:
        ms.append(simple(string, s))
    if num == 1:
        ms.append(rabin_karp(string, s))
    if num == 2:
        ms.append(boyer_mur(string, s))
    if num == 3:
        ms.append(knut_morris_pratt(string, s))
print(max(ms), "вхождений у числа", ms.index(max(ms)))
