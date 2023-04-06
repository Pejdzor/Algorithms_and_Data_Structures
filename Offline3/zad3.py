from zad3testy import runtests

def heapsort(T):
    n=len(T)
    for i in range(n//2 - 1,-1,-1):
        heapify(T,n,i)
    for i in range(n-1,0,-1):
        T[i], T[0]=T[0], T[i]
        heapify(T,i,0)

def heapify(T,n,i):
    larg=i
    l = 2*i + 1
    r = 2*i + 2
    if l<n and T[larg]<T[l]:
        larg=l
    if r<n and T[larg]<T[r]:
        larg=r
    if larg != i:
        T[i], T[larg]=T[larg],T[i]
        heapify(T,n,larg)

def insertsort(T):
    for i in range(1,len(T),1):
        x=T[i]
        j=i-1
        while j>=0 and T[j]>x:
            T[j], T[j+1]=T[j+1], T[j]
            j-=1
        T[j+1]=x


def bucketsort(T):
    mx=max(T)
    buckets=[]
    size=mx/len(T)
    for i in range(len(T)):
        buckets.append([])
    for i in range(len(T)):
        if T[i]/size == len(buckets):
            buckets[len(T)-1].append(T[i])
        else:
            buckets[int(T[i] / size)].append(T[i])
    for i in range(len(buckets)):
        if len(buckets[i])>1:
            if len(buckets[i])<10:
                insertsort(buckets[i])
            else:
                heapsort(buckets[i])
    result=[0 for _ in range(len(T))]
    k=0
    for i in buckets:
        for j in i:
            result[k]+=j
            k+=1
    return result
def SortTab(T,P):
    T=bucketsort(T)
    return T

runtests( SortTab )
