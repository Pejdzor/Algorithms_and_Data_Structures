
# Algorytm tworzy tablicę L[p][max(b)] gdzie komórki L[i][j] określa ile masksymalnie studentów
# można pomieścić w blokach wybudowanych do współrzędnej b=j i koszcie niewiększym niż i.
# Złożoność czasowa algorytmu to O(n*p*max[b]), max(b) to największa współrzędna b w tablicy T
# Złożoność pamięciowa algorytmu to O(p*max[b])

from zad4testy import runtests


def resids(a,b,h):
    return h*(b-a)

def f(S,L,LL,i,p):
    if i<0:
        return 0
    if L[p][i]!=-1:
        return L[p][i]
    maks=0
    j=0
    while S[j][2]<i:
        j+=1
    if S[j][2]>i:
        L[p][i]=f(S, L,LL, i - 1, p)
        return L[p][i]
    while j<len(S) and S[j][2]==i:
        if p>=S[j][3]:
            wartosc = f(S,L,LL,S[j][1]-1,p-S[j][3])+resids(S[j][1],S[j][2],S[j][0])
            if wartosc > maks:
                maks = wartosc
                LL[p][i] = j
        j+=1
    if maks<f(S,L,LL,i-1,p):
        maks=f(S,L,LL,i-1,p)
        LL[p][i] = -1
    L[p][i]=maks
    return L[p][i]

def select_buildings(T,p):
    n=len(T)
    S=sorted(T,key=lambda x: x[2])
    L=[[-1 for _ in range(S[n-1][2]+1)] for _ in range(p+1)]
    LL=[[-1 for _ in range(S[n-1][2]+1)] for _ in range(p+1)]

    for i in range(S[0][2]):
        for j in range(p+1):
            L[j][i]=0
    l=len(L[0])
    for i in range(l):
        f(S,L,LL,i,p)

    R = []
    ii = l-1

    while ii >= 0 and p >= 0:
        num = LL[p][ii]
        if num != -1:
            R.append(num)
            ii = S[num][1]-1
            p -= S[num][3]
        else:
            ii -= 1

    res = []
    for el in R:
        for i in range(len(T)):
            if S[el] == T[i]:
                res.append(i)

    return res
runtests(select_buildings)