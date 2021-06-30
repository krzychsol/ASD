V = 5
def DFS(graph, marked, n, vert, start, count):
    marked[vert] = True

    if n == 0:
        marked[vert] = False
        if graph[vert][start] == 1:
            count = count + 1
            return count
        else:
            return count

    for i in range(V):
        if marked[i] == False and graph[vert][i] == 1:
            count = DFS(graph, marked, n - 1, i, start, count)

    marked[vert] = False
    return count

def countCycles(graph, n):
    marked = [False] * V
    count = 0
    for i in range(V - (n - 1)):
        count = DFS(graph, marked, n - 1, i, i, count)
        marked[i] = True

    return int(count / 2)

graph = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [1, 0, 1, 0, 1],
         [0, 1, 0, 1, 0]]

n = 4
if countCycles(graph,n)>0:
    print("True")
else: print("False")


