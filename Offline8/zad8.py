
# Algorytm poszukuje wszystkich MST przy pomocy algorytmu Kruskala i szuka wyniku, który spełnia założenia zadania.
#  Złożoność czasowa O(N^4*logn), pamięciowa O(n^2)

from zad8testy import runtests
from math import sqrt

def dis(p1,p2):
    f=sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    if f%1>0.0:
        f=f//1 + 1
    return int(f)


class zbior_rozlaczny:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for _ in range(n)]

    def znajdz(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.znajdz(self.parent[x])
        return self.parent[x]

    def polacz(self,x,y):
        x=self.znajdz(x)
        y=self.znajdz(y)
        if self.rank[x]>self.rank[y]:
            self.parent[y]=x
        else:
            self.parent[x]=y
            if self.rank[y]==self.rank[x]:
                self.rank[y]+=1


def highway( A ):
    n=len(A)
    E = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            E.append((i, j, dis(A[i], A[j])))

    E.sort(key=lambda x:x[2])
    naj=float("inf")

    lastval = 0
    lastmax = 0
    for k in range(len(E)):
        if lastmax - E[k][2] > naj:
            continue
        if E[k][2] == lastval and k != 0:
            continue
        lastval = E[k][2]
        count = 0
        B = zbior_rozlaczny(n)
        C = []
        for i in range(k, len(E)):
            a, b, w = E[i]
            if B.znajdz(a) != B.znajdz(b):
                B.polacz(a, b)
                C.append((a, b, w))
                count += 1

        if count == n-1:
            wmax = 0
            wmin = float("inf")
            for x in C:
                wmax = max(wmax, x[2])
                wmin = min(wmin, x[2])

            naj = min(naj, wmax - wmin)
            lastmax = wmax
    return naj


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True)