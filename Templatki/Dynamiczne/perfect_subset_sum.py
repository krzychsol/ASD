
def printAllSubsets(T,sum):
    n = len(T)
    if n == 0 or sum < 0:
        return

    dp = [[0 for _ in range(sum+1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    if T[0] <= sum:
        dp[0][T[0]] = 1

    for i in range(1,n):
        for j in range(sum+1):
            if T[i] <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-T[i]])
            else:
                dp[i][j] = dp[i-1][j]

    if dp[n-1][sum] == 0:
        return None

    p = []
    cnt = 0
    def printSubsetsRec(T, i, sum, p):
        nonlocal cnt
        if i == 0 and sum != 0 and dp[0][sum]:
            p.append(T[i])
            if T[i] == sum:
                cnt+=1
                print(p)
                return

        if i == 0 and sum == 0:
            cnt+=1
            print(p)
            return

        if dp[i-1][sum]:
            tmp = p.copy()
            printSubsetsRec(T,i-1,sum,tmp)

        if sum >= T[i] and dp[i-1][sum-T[i]]:
            p.append(T[i])
            printSubsetsRec(T,i-1,sum-T[i],p)

    printSubsetsRec(T, n - 1, sum, p)
    return cnt

T = [1,2,3,4,5]
sum = 10
print(printAllSubsets(T,sum))