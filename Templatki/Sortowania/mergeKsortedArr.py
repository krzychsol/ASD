def merge(T):
  n = len(T)
  buildheap(T)
  B = []
  while T:
      B.append(T[0][0])
      T[0].pop(0)
      if not T[0]:
          T.pop(0)
          buildheap(T)
      heapify(T,n,0)
  return B

def buildheap(T):
  n = len(T)
  for i in range(parent(n-1),0,-1):
    heapify(T,n,i)

def heapify(T,n,i):
  l = left(i)
  r = right(i)
  m = i
  if l < n and T[l][0] < T[m][0] :
    m = l
    T[m],T[l] = T[l],T[m]
  if r < n and T[r][0] < T[m][0] :
    m = r
    T[m],T[r] = T[r],T[m]
  heapify(T,n,m)

def parent(i):
  return (i-1)//2

def left(i):
  return 2*i +1

def right(i):
  return 2*i +2

T = [[0,1,2,4,5],[0,10,20],[5,15,25]]
print(merge(T))