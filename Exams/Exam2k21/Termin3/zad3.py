from Exams.Exam2k21.Termin3.zad3testy import runtests

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.key = None

def toBinary(x):
    binary = ""
    while x:
        if x%2 == 0:
            binary = "0"+binary
        else:
            binary = "1"+binary
        x //= 2

    n = len(binary)
    return binary, n

def maxim(T, C):
    m = len(C)
    for i in range(m):
        C[i] = toBinary(C[i])

    maxKey = -float("inf")
    for i in range(m):
        string = C[i][0]
        lenStr = C[i][1]
        curr = T

        for j in range(1,lenStr):
            if string[j] == '0':
                curr = curr.left
            else:
                curr = curr.right
        maxKey = max(maxKey,curr.key)

    return maxKey


runtests(maxim)
