#P[i] = (x1,y1,x2,y2) left,down,right,up
from Others.GymKol2.PrzeciecieProstokatow.zad1testy import runtests

def area(P,x):
    result = 0
    n = len(P)

    maxLeft = -float("inf")
    minRight = float("inf")
    minUp = float("inf")
    maxDown = -float("inf")

    for i in range(n):
        if i == x:
            continue
        left, down,right, up = P[i]
        if left > maxLeft:
            maxLeft = left
        if right < minRight:
            minRight = right
        if down > maxDown:
            maxDown = down
        if up < minUp:
            minUp = up

    #print(maxLeft, minRight, maxDown, minUp)
    if maxLeft < minRight and maxDown < minUp:
        result = (minRight-maxLeft)*(minUp-maxDown)
    return result


def rect(P):
    n = len(P)
    maxLeft = [-float("inf"),None]
    minRight = [float("inf"),None]
    minUp = [float("inf"),None]
    maxDown = [-float("inf"),None]

    for i in range(n):
        left,down,right,up = P[i]
        if left > maxLeft[0]:
            maxLeft = [left,i]
        if right < minRight[0]:
            minRight = [right,i]
        if down > maxDown[0]:
            maxDown = [down,i]
        if up < minUp[0]:
            minUp = [up,i]

    #print(maxLeft,minRight,maxDown,minUp)
    result = 0
    idx = 0
    if area(P,maxLeft[1]) > result:
        result = area(P,maxLeft[1])
        idx = maxLeft[1]
    if area(P,minRight[1]) > result:
        result = area(P,minRight[1])
        idx = minRight[1]
    if area(P,maxDown[1]) > result:
        result = area(P,maxDown[1])
        idx = maxDown[1]
    if area(P,minUp[1]) > result:
        result = area(P,minUp[1])
        idx = minUp[1]

    return idx

runtests(rect)