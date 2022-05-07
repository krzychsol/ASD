'''
LONGEST-PALINDROMIC-SUBSEQUENCE
Problem znajdowania najdłuższego podciągu (niekoniecznie spójnego) w stringu, będącego palindromem.
'''

# ALGORYTM:
'''
Zaczynamy z indeksami i na początku oraz j na końcu stringa. Jeśli obie litery są takie same, to zwiększamy długość
podciągu o 1 i przesuwamy oba indeksy, jeśli nie, to przesuwamy indeks i lub j, w zależności, który bardziej sie opłaca. 
'''
#O(n^2)


def LPS(S):
    n = len(S)
    memo = [[None for _ in range(n)] for __ in range(n)]

    def LPS_req(i, j):
        if i == j:
            return 1
        if i > j:
            return 0
        elif S[i] == S[j]:
            if memo[i][j] is None:
                memo[i][j] = 2 + LPS_req(i+1,j-1)
        else:
            if memo[i][j] is None:
                memo[i][j] = max(LPS_req(i+1,j),LPS_req(i,j-1))

        return memo[i][j]

    return LPS_req(0,n-1)

word = "character"
print(LPS(word))