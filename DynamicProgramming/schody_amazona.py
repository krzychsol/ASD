'''
Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji 0;
wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję. Przykład A=[1,3,2,1,0].
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile
sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
'''

#O(n^2)
def jumps(T):
    n = len(T)
    jumps = [0 for _ in range(n)]
    jumps[n-2] = 1

    for i in range(n-3,-1,-1):
        max_jump = T[i]
        for j in range(1,max_jump+1):
            if i+j == n-1:
                jumps[i] += 1
                break
            else:
                jumps[i] += jumps[i+j]

    return jumps

T = [5,3,4,7,0]
print(jumps(T))