
# Algorytm najpierw zamienia daną listę krawędzi na macierz sąsiedztwa. Potem sprawdza maksymalną przepustowość
# wejściową każdego wierzchołka. Wybiera kwadratowo 2 wierzchołki, będące SUPERUJŚCIEM zaczynając od tych, które
# mają największą przepustowość wejściową. Jeśli suma przepustowości wejściowych jest mniejsza, niż znaleziony
# do tej pary największy przepływ, to algorytm przerywa działanie, ponieważ nie można znaleźć lepszego przepływu
# Złożoność czasowa: O(n^2*v^2), złożoność pamięciowa O(v^2)

from zad9testy import runtests
from collections import deque


def matrix(G):
    best = 1
    for i in range(len(G)):
        best = max(best, G[i][0], G[i][1])
    A = [[0 for _ in range(best + 2)] for _ in range(best + 2)]
    for i in G:
        A[i[0]][i[1]] = i[2]
    return A



def findpath(G, s, t):
    par = [None for _ in range(len(G))]
    visit = [False for _ in range(len(G))]
    cap = [0 for _ in range(len(G))]
    p = deque()
    p.append(s)
    while len(p) > 0:
        v = p.popleft()
        for i in range(len(G[v])):
            if G[v][i] > cap[i] and not visit[i]:
                par[i] = v
                cap[i] = G[v][i]
                p.append(i)
        visit[v] = True
    if par[t] == None:
        return None,0
    path = []
    bestcap = cap[t]
    while t is not None:
        path.append(t)
        if t != s:
            bestcap = min(bestcap, cap[t])
        t = par[t]
    path.reverse()

    return path, bestcap


def maxflow(G, s):
    A = matrix(G)
    out=0
    for i in range(len(A)):
        if A[s][i]!=0:
            out+=1
    if out == 1:
        return sum(A[s])
    t=len(A)-1
    vin=[(i,0) for i in range(len(A)-1)]
    for e in G:
        vin[e[1]]=(e[1],vin[e[1]][1]+e[2])
    vin.sort(key=lambda x:x[1],reverse=True)
    bestflow=0
    for i in range(len(vin)-2):
        for j in range(i+1,len(vin)-1):
            if vin[j][1]+vin[i][1]>bestflow:
                B = matrix(G)
                A[vin[i][0]][t]=B[vin[i][0]][t]=float('inf')
                A[vin[j][0]][t]=B[vin[j][0]][t]=float('inf')
                C = [[0 for _ in range(t+1)] for _ in range(t+1)]
                path, cap = findpath(B, s, t)
                while path is not None:
                    for h in range(len(path)-1):
                        if A[path[h]][path[h+1]]!=0:
                            B[path[h]][path[h+1]]-=cap
                            B[path[h+1]][path[h]]+=cap
                            C[path[h]][path[h + 1]] += cap
                        else:
                            B[path[h]][path[h + 1]] += cap
                            B[path[h + 1]][path[h]] -= cap
                            C[path[h]][path[h + 1]] += cap
                    path, cap = findpath(B, s, t)
                flow=0
                for k in range(len(B)):
                    if C[k][t]!=float('inf'):
                        flow+=C[k][t]

                bestflow=max(bestflow,flow)

                A[vin[i][0]][t] = 0
                A[vin[j][0]][t] = 0
    return bestflow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
