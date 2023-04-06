
# Algorytm przechodzi liniowo po tablicy z wartościami paliwa i zapisuje do tablicy P indeksy pól oraz wartość
# ropy takie się na nich znajdowały. Potem, gdy zabraknie mu paliwa, sprawdza na jakim polu miniętym znajdowała się
# największa wartość ropy i zapisuje indeks pola do tablicy L. Złożoność czasowa O(nlogn), złożoność pamięciowa O(n)

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    P=PriorityQueue()
    R=[]
    j=0
    e=0
    while j<len(T)-1 and e>=0:
        if T[j]!=0:
            P.put((-1*T[j],j))
        if e==0:
            ropa=P.get()
            e=-1*ropa[0]
            R.append(ropa[1])
        j+=1
        e-=1
    R=sorted(R)
    return R

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )