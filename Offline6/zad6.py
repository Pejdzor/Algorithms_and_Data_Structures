
# Algorytm odnajduje najkrótszą ścieżkę od s do t. Jeśli istnieje tylko 1 krawędź wchodząca
# do t, to algorytm usuwa ostatnią krawędź między s i t. Jeśli jest więcej takich ścieżek
# Jeśli jest więcej, to na podstawie ścieżek tworzy graf z samych najkrótszych ścieżek i próbuje
# go rozspójnić poprzez usunięcie mostu. Jeśli taki most istnieje, to go zwraca, jeśli nie,
# to zwraca NONE. Złożoność czasowa O(E(V+E)). Złożoność Pamięciona O(V)
from zad6testy import runtests
from collections import deque


def bfs(G, s):
    q = deque()
    g = len(G)
    vis = [False for _ in range(g)]
    dist = [float("inf") for _ in range(g)]
    par = [[] for _ in range(g)]
    q.append(s)
    dist[s] = 0
    while len(q) > 0:
        v = q.popleft()
        if not vis[v]:
            vis[v] = True
            for i in G[v]:
                if not vis[i]:
                    q.append(i)
                    d = dist[v] + 1
                    if d < dist[i]:
                        dist[i]=d
                        par[i]=[v]
                    elif d == dist[i]:
                        dist[i]=d
                        par[i].append(v)
                        par[v].append(v)
    return par


def graphify(G, T, u):
    g=len(G)
    A=[[] for _ in range(g)]
    vis =[False for _ in range(g)]
    q=deque()
    q.append(u)
    while len(q)>0:
        v=q.popleft()
        if not vis[v]:
            vis[v] = True
            for x in T[v]:
                if not vis[x]:
                    A[v].append(x)
                    A[x].append(v)
                    q.append(x)
    return A

def dfs(G):
    time=0
    par=[None for _ in range(len(G))]
    cycl=[len(G) for _ in range(len(G))]
    vis=[False for _ in range(len(G))]
    bridge=None
    def visitDFS(G, P, T, V, u):
        nonlocal time
        time+=1
        V[u]=True
        T[u]=time
        naj=T[u]
        for x in G[u]:
            if not V[x]:
                P[x]=u
                visitDFS(G,P,T,V,x)
        for x in G[u]:
            if x!=P[u]:
                naj=min(naj,T[x])
        if T[u]==naj:
            nonlocal bridge
            if bridge is None:
                bridge=(u,P[u])
        T[u]=naj
    for x in range(len(G)):
        if not vis[x]:
            visitDFS(G,par,cycl,vis,x)
    if bridge[1]==None:
        return None
    return bridge


def longer(G, s, t):
    A = bfs(G, s)
    if len(A[t])==1:
        return (A[t][0],t)
    g = graphify(G, A, t)
    bridge=dfs(g)
    return bridge


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
