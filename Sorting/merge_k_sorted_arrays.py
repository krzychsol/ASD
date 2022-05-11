'''
    Zaproponuj algorytm scalający k posortowanych
    tablic w jedną posortowaną tablicę. Łączna liczba
    elementów we wszystkich tablicach wynosi n.
    Algorytm powinien najlepiej działać w czasie
    O(n*log(k)).
'''


from collections import deque
import heapq
from random import randint

max_value = 100

def generate_data(n, k):
    lists = [[] for i in range(k)]
    while n >= 0:
        list_index = randint(0, k - 1)
        lists[list_index].append(randint(0, max_value))
        n -= 1

    # uzywamy kolejki by moc sciagac w czasie O(1)
    lists = [deque(sorted(lists[i])) for i in range(k)]
    return lists


def print_lists(lists):
    for x in lists:
        print(list(x))

def merge_lists(lists,n):
    k = len(lists)
    firsts = []

    for i in range(k):
        if lists[i]:
            firstEl = lists[i][0]
            firsts.append((firstEl,i))

    heapq.heapify(firsts)
    result = []
    res_len = 0

    while res_len < n:
        elem,index = heapq.heappop(firsts)
        lists[index].popleft()
        if lists[index]:
            new_el = lists[index][0]
            heapq.heappush(firsts,(new_el,index))

        result.append(elem)
        res_len += 1

    return result


lists = generate_data(150,11)
print_lists(lists)
print(merge_lists(lists,150))