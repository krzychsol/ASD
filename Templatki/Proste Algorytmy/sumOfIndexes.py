'''
Dana jest posortowana tablica A[1...n] i liczba x.
Prosze napisac program, ktory stwierdza,
czy istnieja indeksy i oraz j takie, ze A[i] + A[j] = x
'''

def indeksSum(A,x):
    left = 0
    right = len(A) - 1
    while left < right:
        if x == A[left] + A[right]:
            return True
        elif x > A[left] + A[right]:
            left += 1
        else:
            right -= 1
    return False
