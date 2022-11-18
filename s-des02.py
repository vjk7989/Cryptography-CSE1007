import itertools


def shft(s):
    res = ""
    for i in range(len(s) - 1):
        res += s[i + 1]
    res1 = res + s[0]
    return res1


def p(i1, i2):
    ls1 = []
    for i in range(len(i1)):
        ls1.append(i1[i])

    l2 = []
    for j in range(len(i2)):
        l2.append(ls1[i2[j] - 1])

    return l2


# key0 = "1010110111"
def keFin(key0):
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

    key00 = p(key0, p10)
    key = ""
    for i in range(len(key00)):
        key += key00[i]

    s1 = key[0:5]  # split into 2
    s2 = key[5:]

    ss1 = shft(s1)  # first shift
    ss2 = shft(s2)

    new_key = ss1 + ss2
    p88 = [6, 3, 7, 4, 8, 5, 10, 9]
    print("key 1 : ", p(new_key, p88))
    key1 = p(new_key, p88)
    return key1


def exRRCheck(s, s1):
    st = ""
    for i in range(len(s)):
        if (s[i] == '0'):
            if (s1[i] == "1"):
                st += '1'
            else:
                st += '0'
        elif (s[i] == '1'):
            if (s1[i] == "1"):
                st += '0'
            else:
                st += '1'
    return st


def keyGen():
    ls = list(itertools.product([0, 1], repeat=10))
    return ls


def lsToStr(s):
    str1 = ""
    for i in s:
        str1 += str(i)
    return str1


def binRet(s):
    if s == "00":
        return 0
    elif s == "01":
        return 1
    elif s == "10":
        return 2
    elif s == "11":
        return 3
    return -1


def n2Bin(s):
    res = ""
    if s == '0':
        res = "00"
    elif s == '1':
        res = "01"
    elif s == '2':
        res = "10"
    elif s == '3':
        res = "11"
    return res


def s_Mat(s):
    s0 = [['1', '0', '3', '2'],
          ['3', '2', '1', '0'],
          ['0', '2', '1', '3'],
          ['3', '1', '3', '2']]

    s1 = [['0', '1', '2', '3'],
          ['2', '0', '1', '3'],
          ['3', '0', '1', '0'],
          ['2', '1', '0', '3']]
    p2 = s[5:]
    p1 = s[0:5]
    r1 = p1[0] + p1[-1]
    r2 = p2[0] + p2[-1]
    c1 = p1[1] + p1[-2]
    c2 = p2[1] + p2[-2]
    k = s0[binRet(r1)][binRet(c1)]
    k1 = s1[binRet(r2)][binRet(c2)]
    l = n2Bin(k) + n2Bin(k1)
    return l


def nxtT(peP, k1):
    s = exRRCheck(peP, ke)


# pT = "10101011"

def ltoSt(l):
    s = ""
    for i in range(len(l)):
        s += l[i]
    return s


def slay(pT):
    iP = [2, 6, 3, 1, 4, 8, 5, 7]
    pst_iP = p(pT, iP)
    rK = pst_iP[4:]
    eP = [4, 1, 2, 3, 2, 3, 4, 1]
    post_eP = p(rK, eP)
    s_Val = s_Mat(post_eP)
    result = s_Val + ltoSt(rK)
    return result


for i in range(len(keyGen())):
    l = lsToStr(keyGen()[i])
    v = "01110011"
    t = slay(l)
    print(t)
