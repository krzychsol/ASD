def covid(T,k):
    last = -1  # zeby pierwsze spr bylo dla miasta o indeksie 0
    counter = 0
    notProtected = last + k
    while last < len(T) - k:  # jesli maszyna jest na ktoryms z ostatnich k miejsc to ochroni reszte miast po niej, wiec nie musimy dalej sprawdzac
        if notProtected >= len(T):  # jesli ostatnie niechronione jest za tablica, to zaczynam od ostatniego
            notProtected = len(T) - 1
        while T[notProtected] != 1 and notProtected >= last + 1:
            notProtected -= 1
        if notProtected == last:  # tzn ze nie bylo maszyny
            return -1
        else:
            # na miejscu not protected stawiamy maszyne
            last = notProtected
            notProtected += 2 * k - 1  # kolejne k-1 chronimy, a maksymalnie niechronione moze byc jeszcze o kolejne k dalej(tam najdalej maszyna)
            counter += 1

    return counter

T = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]
k = 3
print(covid(T,k))