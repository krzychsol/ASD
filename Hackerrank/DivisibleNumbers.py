
def haveZeros(x):
    tmp = x
    while tmp > 0:
        val = tmp%10
        if val == 0:
            return False
        tmp = tmp//10
    return True

def sumOfdigits(x):
    sum = 0
    tmp = x
    while tmp > 0:
        sum += tmp%10
        tmp = tmp//10
    return sum

def productOfDigits(x):
    pr = 1
    tmp = x
    while tmp > 0:
        pr *= tmp%10
        tmp = tmp//10
    return pr

def divisibleNumbers(n):
    flag = True
    for m in range(1,n+1):
        if n%m == 0:
            flag = haveZeros(m)
            flag = (sumOfdigits(m)>= productOfDigits(m))
            if flag:
                return m

    return -1

print(divisibleNumbers(32))