def quick_sort(T,l,p):
  n = len(T)

  stos = []
  stos.append((0,n-1))

  while len(stos)>0:
    l,p=stos.pop()

    i = l
    j = p

    x = T[(l+p)//2]
    while i<=j:
      while T[i] < x:
        i+=1
      while T[j]>x:
        j-=1
      if i<=j:
        T[j],T[i]=T[i],T[j]
        i+=1
        j-=1
    if l < j:
      stos.append((l,j))
    if i<p:
      stos.append((i,p))

T  = [2,5,3,1,6,8,5,8]
quick_sort(T,0,len(T)-1)
print(T)