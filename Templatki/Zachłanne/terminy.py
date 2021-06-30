def jobscheduling(A, t):
    n = len(A)
    A = sorted(A,key=lambda x:x[1],reverse=True)
    print(A)

    result = [False] * t
    job = [-1] * t

    for i in range(len(A)):
        for j in range(min(t - 1, A[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = i
                break
    print(job)

A = [[7, 202],[ 5, 29],[ 6, 84],[ 1, 75],[ 2, 43]]
jobscheduling(A, 3)

#########

def func(T):
    length = len(T)
    array = T
    sorter = lambda x: (x[0])
    array = sorted(array, key=sorter, reverse=True)
    counter = 0
    time = array[0][0]
    while time > 0:
        i = 0
        curr = 0
        while i < length:
            if array[i][0] >= time:
                if array[i][1] > curr:
                    curr = array[i][1]
                    index = i
            else:
                i = length
            i += 1
        counter += curr
        array[index][1] = 0
        time -= 1
    return counter

T = [[1, 5], [1, 10], [2, 13], [2, 12]]