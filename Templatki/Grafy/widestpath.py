# Python3 implementation of the approach

# Function to prthe required path
def printpath(parent, vertex, target):
    # global parent
    if (vertex == 0):
        return
    printpath(parent, parent[vertex], target)
    print(vertex, end="\n" if (vertex == target) else "--")


# Function to return the maximum weight
# in the widest path of the given graph
def widest_path_problem(Graph, src, target):
    # To keep track of widest distance
    widest = [-10 ** 9] * (len(Graph))

    # To get the path at the end of the algorithm
    parent = [0] * len(Graph)

    # Use of Minimum Priority Queue to keep track minimum
    # widest distance vertex so far in the algorithm
    container = []
    container.append((0, src))
    widest[src] = 10 ** 9
    container = sorted(container)
    while (len(container) > 0):
        temp = container[-1]
        current_src = temp[1]
        del container[-1]
        for vertex in Graph[current_src]:

            # Finding the widest distance to the vertex
            # using current_source vertex's widest distance
            # and its widest distance so far
            distance = max(widest[vertex[1]],
                           min(widest[current_src], vertex[0]))

            # Relaxation of edge and adding into Priority Queue
            if (distance > widest[vertex[1]]):
                # Updating bottle-neck distance
                widest[vertex[1]] = distance

                # To keep track of parent
                parent[vertex[1]] = current_src

                # Adding the relaxed edge in the prority queue
                container.append((distance, vertex[1]))
                container = sorted(container)
    printpath(parent, target, target)
    return widest[target]


# Driver code
if __name__ == '__main__':
    # Graph representation
    graph = [[] for i in range(5)]
    no_vertices = 4
    # Adding edges to graph

    # Resulting graph
    # 1--2
    # |  |
    # 4--3

    # Note that order in pair is (distance, vertex)
    graph[1].append((1, 2))
    graph[1].append((2, 4))
    graph[2].append((3, 3))
    graph[4].append((5, 3))

    print(widest_path_problem(graph, 1, 3))