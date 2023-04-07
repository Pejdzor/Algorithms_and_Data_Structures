
# Algorytm opiera się na zasadzie działania DFS. Uruchamiam algorytm przeszukiwania wgłąb
# i jeśli dojdzie do końca, zwraca numer wierzchołka i w każdym wyższym wywołaniu, wydłuża rozwiązanie o zwróconą listę
# w funkcji głównej sprawdza, czy dla 1 wierzchołka założenia zadania są spełnione
# Złożoność czasowa O(2^v) a pamięciowa O(v), gdzie v oznacza liczbę miast
from zad7testy import runtests

def check(G,V,s,p,v,n):
    flag=0
    #warunek końca
    if  n==len(G):
        for i in G[v][0]:
            if i==p:
                flag=1
        for i in G[v][flag]:
            if i==s:
                return [v]
        return None
    #sprawdzam z której bramy przybywam
    for i in G[v][0]:
        if i==p:
            flag = 1
    sol=[v]
    #sprawdzam rozwiązanie dla bramy, którą powinienem wyjść
    for i in G[v][flag]:
        if not V[i]:
            V[i]=True
            res=check(G,V,s,v,i,n+1)
            if res is not None:
                sol.extend(res)
                return sol
            V[i]=False
    return None


def droga( G ):
    V=[False for _ in range(len(G))]
    res=None
    # algorytm DFS, który zwraca listę wierzchołków w kolejności do odwiedzenia
    for i in range(len(G)):
        V[i]=True
        res=check(G,V,i,None,i,1)
        if res!=None:
            break
        V[i]=False
    # sprawdzam, czy 1 wierzchołek spełnia założenia
    if res is not None:
        count=0
        for i in G[res[0]][0]:
            if i==res[1] or i==res[-1]:
                count+=1
        if count == 1:
            return res
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )