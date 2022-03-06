# Znajdowanie min i max w tablicy wykonując 1,5n porownan

def min_max(T):
    n = len(T)
    min_el = float("inf")
    max_el = -float("inf")

    if n & 1:
        n = n - 1

    for i in range(0, n, 2):
        if T[i] < T[i + 1]:  # 1st comparison
            curr_min = T[i]
            curr_max = T[i + 1]
        else:
            curr_min = T[i + 1]
            curr_max = T[i]

        if curr_min < min_el:  # 2nd comparison
            min_el = curr_min
        if curr_max > max_el:  # 3rd comparison
            max_el = curr_max

    if len(T) & 1:
        min_el = min(min_el, T[len(T) - 1])
        max_el = max(max_el, T[len(T) - 1])

    return min_el, max_el


A = [-10, 1, 2, 3, -100, 100, 23, 4]
print(min_max(A))
