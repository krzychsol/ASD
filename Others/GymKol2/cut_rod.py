'''
Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach
wyrażoną zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n
metrów. Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.
'''

# w tablicy dp pod indeksem i trzymamy maksymalny zysk z pocięcia kawałka pręta o długości i, a w tablicy price
# mamy pod price[i] cenę kawałka długości i
# sprawdzamy coraz dłuższe pręty - "odcinamy" kawałek o długości j, a następnie odczytujemy zmaksymalizowany
# zysk z tablicy dp  - już wcześniej obliczony

def cut_rod(price,n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0

    for length in range(1,n+1):
        max_val = -float("inf")
        for j in range(length):
            max_val = max(max_val,price[j]+dp[length-1-j])

        dp[length] = max_val
    print(dp)
    return dp[n]

price = [1,5,8,9,10,17,17,20]
print(cut_rod(price,len(price)))