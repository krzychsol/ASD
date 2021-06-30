'''
Zaproponuj algorytm, który w czasie O(nlog(n)) posortuje stos o rozmiarze n. Dozwolone jest tylko wykorzystywanie operacji udostępnionych przez interfejs stosu:
 push(), pop(), top(), isEmpty(), oraz dodatkowych stosów.
'''

from random import randint

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

def sortstack(S):
    n = len(S.items)
    if n <= 1:
        return S

    mid = n//2
    S1 = Stack()
    S2 = Stack()
    for i in range(mid):
        S1.push(S.top())
        S = S.pop()
    for i in range(mid):
        S2.push(S.top())
        S = S.pop()
    print(S.isempty)

S = Stack()
n = 20
for i in range(n):
    S.push(randint(1,15))
sortstack(S)
