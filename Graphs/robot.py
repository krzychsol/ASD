from zad2testy import runtests
from queue import PriorityQueue


def robot(L, A, B):
    r = len(L)
    c = len(L[0])
    d = [[[[float("inf")
            for x in range(c)]
           for y in range(r)]
          for o in range(4)]
         for v in range(3)]

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    speed = [60, 40, 30]
    Q = PriorityQueue()
    Q.put((0, 0, 0, A[1], A[0]))  # time speed dir-ion posOX posOY

    while not Q.empty():
        time, v, o, x, y = Q.get()

        if (y, x) == B:
            return time

        if d[v][o][x][y] < float("inf"):
            continue
        else:
            d[v][o][x][y] = time

        if L[x + dirs[o][0]][y + dirs[o][1]] != 'X':
            Q.put((time + speed[v], min(v + 1, 2), o, x + dirs[o][0], y + dirs[o][1]))
        Q.put((time + 45, 0, (o + 1) % 4, x, y))
        Q.put((time + 45, 0, (o + 3) % 4, x, y))


runtests(robot)
