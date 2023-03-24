from zad1testy import Node,runtests;

def heapify(arr, n, i):
    low = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and (arr[l] is not None and (arr[low] is None or arr[l].val < arr[low].val)):
        low = l
    if r < n and (arr[r] is not None and (arr[low] is None or arr[r].val < arr[low].val)):
        low = r
    if low != i:
        arr[i], arr[low] = arr[low], arr[i]
        heapify(arr, n, low)


def SortH(p, k):
    guard = Node()
    guard.next = p
    if k == 0:
        return p
    if k == 1:
        bubble = [None, None]
        for i in range(2):
            bubble[i] = p
            if p is not None:
                p = p.next
        if bubble[0] is not None:
            if bubble[1] is not None and bubble[0].val > bubble[1].val:
                bubble[1], bubble[0] = bubble[0], bubble[1]
        last = guard
        last.next = bubble[0]
        last = last.next
        while p is not None:
            bubble[0] = p
            p = p.next
            if bubble[0] is not None:
                if bubble[1] is not None and bubble[0].val > bubble[1].val:
                    bubble[1], bubble[0] = bubble[0], bubble[1]
            last.next = bubble[0]
            last = last.next
        if bubble[1] is not None:
            last.next = bubble[1]
            last = last.next
        last.next = None
        tmp = guard.next
        del guard
        return tmp

    heap = [None for _ in range(k + 1)]
    for i in range(k + 1):
        heap[i] = p
        if p is not None:
            p = p.next
    for i in range((k + 1) // 2, -1, -1):
        heapify(heap, k + 1, i)
    last = guard
    last.next = heap[0]
    last = last.next
    while p is not None:
        heap[0] = p
        p = p.next
        heapify(heap, k + 1, 0)
        last.next = heap[0]
        last = last.next
    heap[0] = None
    for i in range((k + 1) // 2, -1, -1):
        heapify(heap, k + 1, i)
    for i in range(k, 0, -1):
        heap[i], heap[0] = heap[0], heap[i]
        heapify(heap, i, 0)
    for x in range(len(heap) - 1, -1, -1):
        if heap[x] is not None:
            last.next = heap[x]
            last = last.next
    last.next = None
    tmp = guard.next
    del guard
    return tmp



runtests(SortH)