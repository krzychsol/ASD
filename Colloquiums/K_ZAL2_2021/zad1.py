from zad1testy import runtests
from collections import deque

def tanagram(x, y, t):
    if len(x) != len(y):
        return False

    pos = [deque() for _ in range(26)]
    for i,c in enumerate(y):
        pos[ord(c)-97].append(i)
    for i,c in enumerate(x):
        closest = pos[ord(c)-97].popleft()
        if abs(closest-i)>t:
            return False
    return True

runtests( tanagram )