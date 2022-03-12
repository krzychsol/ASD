from collections import deque

def isSafe(map, x, y,visited):
    return (x >= 0) and (x < len(visited)) and \
        (y >= 0) and (y < len(visited[0])) and \
        (map[x][y] == 1 and not visited[x][y])

def BFS(G,visited,i,j):
    q = deque()
    q.append((i,j))

    visited[i][j] = True

    while q:
        x,y = q.popleft()
        for k in range(8):
            if isSafe(G,x+row[k],y+col[k],visited):
                visited[x+row[k]][y+col[k]] = True
                q.append((x+row[k],y+col[k]))

map = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]

N = len(map)
visited = [[False for _ in range(N)]for _ in range(N)]
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
island = 0

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            BFS(map,visited,i,j)
            island += 1

print(island)