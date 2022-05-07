#mamy las postawiany na osi OX gdzie na kazdej liczbie na osi znajduje sie drzewo.
#mamy liste profitow jakie mozemy dostac ze scięcia kazdego drzewa
#nie mozemy siac dwoch sasiadujacych drzew
#jaki jest max profit

P = [4,2,2,4] # lista profitów

def cut_forset(P):
    n = len(P)
    t2 = P[0] #zysk z sciecia 1 drzewa
    t1 = max(P[0],P[1]) #maksimum z zysków ze ścięcia 1 i 2 drzewa
    for i in range(2,n):
        t1,t2 = max(t2+P[i],t1),t1
    return t1

r = cut_forset(P)
print(r)