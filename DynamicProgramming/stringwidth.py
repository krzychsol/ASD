from math import inf
#nieskonczone
def shorteststr(S,t):
    n = len(t)
    f = [ -inf ] * n
    for i in range(n):  # dynamic programming, fill array bottom-up
        for s in S:  # check every word
            if i >= len(s):
                substr = t[i - len(s) : i + 1]  # substring ending at current index i, +1, since it’s [start, end)
                if s == substr:  # check if we can use our word
                    f[i] = max(f[i], min(len(s), f[i - len(s)]))  # the longest (max) width, check shortest (min) s_i
    return f[-1]

S = ["ab","abab","ba","bab","b"]
t = "ababbab"
print(shorteststr(S,t))
