from random import randint

#COMPLEXIBILITY [ O(n) ] - MOST EFFICIENT :)

#LEADER SEARCHING-----------------------------------------------------------------
def leader(T):
    #FIND CANDIDATE FOR LEADER
    n = len(T)
    lid = T[0]
    cnt = 1
    for i in range(1,n):
        if cnt == 0:
            lid = T[i]
            cnt = 1
        else:
            cnt += 1 if (T[i]  == lid) else -1

    #CHECK IF CANDIDATE IS LEADER
    if cnt == 0:
        return None
    else:
        cnt = 0
        for i in range(n):
            if T[i] == lid:
                cnt += 1

    if cnt>=n/2:
        return lid
    else:
        return None

#DRIVER CODE SECTION-------------------------------------------------------

T = [1,1,1,1,2,2,1,1,2,2,1]
print(leader(T))
