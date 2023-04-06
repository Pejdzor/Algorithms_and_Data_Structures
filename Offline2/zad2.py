
from zad2testy import runtests


def mergesort(L):
    if len(L) > 1:
        v = len(L) // 2
        l = L[:v]
        r = L[v:]
        mergesort(l)
        mergesort(r)
        merge(L, l, r)


def merge(L, l, r):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i][0] < r[j][0] or (l[i][0] == r[j][0] and l[i][1] >= r[j][1]):
            L[k] = l[i]
            i += 1
        else:
            L[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        L[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        L[k] = r[j]
        j += 1
        k += 1


def depth(L):
    mergesort(L)
    maks = 0
    k = 0
    flag = True
    while flag:
        i = k
        c = 0
        flag = False
        for j in range(i + 1, len(L), 1):
            if L[i][1] >= L[j][1]:
                c += 1
            else:
                if not flag:
                    flag = True
                    k = j
        maks = max(maks, c)
    return maks


runtests(depth)
