#TANKOWANIE CZOŁGU
# A - minimalna liczba tankowan ,aby dotrzec do konca
# Zachłannie jedziemy czołgiem najdalej jak możemy i tam tankujemy
def mintank( S , L ):
    n = len(S)
    tankNum = 0
    prev = 0
    for i in range(n):
        if S[i] - prev > L:
            prev = S[i-1]
            tankNum += 1

    if S[n-1]-prev > L:
        return None
    return tankNum

# B1 - minimalny koszt dotarcia do konca - tankujemy ile chcemy litrow na stacji
def mincost1(L, s, p):
    cost = 0
    i = 0
    x = 0
    curr = L
    while i != len(s) - 1:
        cheap = float("inf")
        for j in range(i+1, len(s)):
            if s[j]-s[i] > L: break
            if p[i] > p[j]:
                x = j
                cost += p[i] * (min(max(0, s[x] - s[i] - curr), s[-1] - s[i]))
                curr += max(0, s[x] - s[i] - curr)
                break
            if cheap > p[j]:
                cheap = p[j]
                x = j
        if p[x] > p[i]:
            cost += p[i] * (min(L - curr, s[-1] - s[i]))
            curr = L
        curr = curr - (s[x] - s[i])
        i = x
    print(cost)

# B2 - minimalny koszt dotarcia do konca - jeśli tankujemy to do pełna
def mincost2(L, s, p):
    F = [float("inf")]*len(s)
    F[0] = 0
    res = float("inf")
    for i in range(1, len(s)):
        j = i-1
        while j != -1 and s[i] - s[j] <= L:
            F[i] = min(F[i], F[j]+p[i]*(s[i]-s[j]))
            j -= 1
        if s[i]+L >= s[-1]:
            res = min(res, F[i])
    print(res)

L = 14
S = [0, 1, 9, 15, 16, 17, 27, 28]
P = [0, 1, 100, 10, 15, 1, 30, 0]

print(mintank(S,L))
mincost1(L,S,P)
mincost2(L,S,P)

####################
# A

def A(max_fuel, S, finish):
    curr_position = 0
    counter = 0
    i = 0
    while curr_position + max_fuel < finish:
        if i == len(S):
            counter += 1
            break

        if S[i] - curr_position > max_fuel:
            curr_position = S[i-1]
            counter += 1

        i += 1

    return counter

# B(2)

def minimal_cost(S, P, t, L):
    F = [(float('inf'), 0)] * (t + 1)
    for i in range(L + 1):
        F[i] = (0, L - i)

    for i in range(1, len(S)):
        k = S[i]
        for j in range(k + 1, min(k + L + 1, t + 1)):
            if j > L:
                new = F[k][0] + ((L - F[k][1]) * (P[i]))
                fuel_left = L - (j - k)
                if new < F[j][0]:
                    F[j] = (new, fuel_left)

    if F[t][0] == float('inf'):
        return -1
    return F[t][0]

# B(2)
def price_always_min(S, P, L, t):
    left = L
    n = len(S)
    price = 0
    curr = 0
    while (curr < n):
        #i - sprawdzam kazda nastepna stacje po curr
        i = curr + 1
        #sprawdzam nastepne stacje tak dlugo jak nie zachodzi jeden z 3 warunkow
        #1. jestem nadal w tablicy
        #2. mam wystarczajaco duzo paliwa w baku zeby dojechac
        #3. stacja ktora "sprawdzam" jest drozsza od obecnej
        while (i < n and S[i] - S[curr] <= left and P[i] >= P[curr]):
            i += 1
        #scenariusz 1 - koniec tablicy
        if i == n:
            #jesli moge dojechac do konca to nie ma problemu, nic nie robie
            if left >= t - S[curr]:
                break
            #jesli NIE moge dojechac do konca z obecnym paliwem
            # ale starczy mi jesli dotankuje to tankuje (bo i tak ta stacja na ktorej jestem
            #jest najtansza pozostala) gdzie stoje i jade do konca
            elif L >= t - S[curr]:
                price += (L - left)*P[curr]
                break
            #jesli mimo tankowania mi nie starczy to tankuje tutaj i przesuwam sie
            #na nastepna stacje, potem robie to samo
            else:
                price += (L - left) * P[curr]
                left = L-S[i-1]+S[curr]
                curr = i-1
        #jesli nadal jestem w tablicy, ale w zasiegu pozostalego paliwa nie
        #ma tanszej stacji to tankuje tutaj gdzie jestem
        elif S[i] - S[curr] > left:
            price += (L - left)*P[curr]
            left = L - S[curr+1] + S[curr]
            curr = curr+1
        #jesli w zasiegu pozostalego paliwa jest tansza stacja to nie tankuje
        #jade tam
        elif P[i] < P[curr]:
            left = left - (S[i] - S[curr])
            curr = i

    return(price)
