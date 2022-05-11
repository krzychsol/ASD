'''
Proszę opisać algorytm dla następującego problemu: dana jest tablica A zawierająca
n przedziałów. Elementy tablicy A opisują przedziały otwarte. Dana
jest także liczba t. Zadanie polega na wypisaniu t lub mniej przedziałów, których suma daje spójny
przedział o maksymalnej długości.
'''

# ALGORYTM:
'''
Sortujemy przedziały po początkach, następnie dzielimy je na grupy przedziałów, których sumy są spójne.
Następnie w każdej z grup rozważamy t przedziałów leżacych obok siebie (jeżeli grupa jest mniej liczna to 
bierzemy wszystkie; gąsienicą od 0 do n-t). Jeżeli zazębiają sę wiecej niż 
2 przedziały to dobieramy tylko ten kończący się najdalej (mamy pewność, że poprzedzające są w sumie
krótsze). Gdy już weźmiemy t (lub mniej) przedziałów sprawdzamy jaką długość ma ich suma i jeżeli
jest taka potrzeba, to aktualizujemy najdłuższą dotychczas znalezioną sumę i przedziały, które ją tworzą, 
by móc je potem wypisać. 
'''

#niedokonczona implementacja

def makeGroups(A):
    groups = []
    g_idx = 0
    n = len(A)
    idx = 0
    while True:
        groups.append([])
        groups[g_idx].append(A[idx])

        while idx+1 < n and A[idx+1][0] <= A[idx][1]:
            groups[g_idx].append(A[idx+1])
            idx += 1

        idx += 1
        g_idx += 1
        if idx == n-1:
            groups.append([A[idx]])

        if idx >= n:
            break


    return groups

def intervals(A,t):
    A = sorted(A,key=lambda x:x[0])
    groups = makeGroups(A)
    max_len = 0
    res = []

    for group in groups:
        cnt = 0
        start = group[0][0]
        end = group[0][1]
        tmp_res = [group[0]]

        for i in range(1,len(group)):
            if cnt >= t:
                break
            end = max(end,group[i][1])
            cnt += 1
            if end-start > max_len:
                max_len = end-start
                tmp_res.append(group[i])




A = [(1,3),(3,4),(3,7),(9,10),(13,14),(14,16)]
print(makeGroups(A))