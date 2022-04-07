'''
ZADANIE: znalezc najwieksza laczna sume 'funu' osob bioracych udzial w imprezie - nie chemy zeby bezposredni
podwladny i przelozony byli jednoczesnie obecni
'''
#O(n)

class Person:
    def __init__(self,name,fun):
        self.fun = fun
        self.name = name
        self.emp = [] #lista podwladnych
        self.f = -1 #wartosc najlepszej jamby zakorzenionej w tym wierzcholku drzewa
        self.g = -1 #wartosc najlepszej jamby wiedzac ze ten pracownik nie idzie
        self.going = None #czy idzie na impreze

def g(v):
    if v.g != -1: return v.g

    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g

def f(v):
    if v.f != -1: return v.f

    f1 = g(v)
    f2 = v.fun
    for u in v.emp:
        f2 += g(u)
    v.f = max(f1,f2)
    return v.f

def party(A):
    n = len(A)
    idx = 0
    while idx < n:
        person = A[idx]
        if person.f > person.g:
            person.going = True
            idx += 1
            for emp in person.emp:
                emp.going = False
                idx += 1
        else:
            person.going = False
            idx += 1
            for emp in person.emp:
                if emp.f > emp.g:
                    emp.going = True
                    idx += 1
                else:
                    emp.going = False
                    idx += 1



# tworze obiekty (osoby)

a=Person('Franek',3)
b=Person('Basia',5)
c=Person('Sylwia',2)
d=Person('Karol',5)

# reszta nie ma podwladnych
e=Person('Kornel',4)
f1=Person('Monika',3)
g1=Person('Kuba',6)
h=Person('Kacper',2)
i=Person('Maria',6)

a.emp=[b,c,d]
b.emp=[e]
c.emp=[f1,g1]
d.emp=[h,i]

arr=[a,b,c,d,e,f1,g1,h,i] #mam cale drzewo w tablicy (od gory wierszami (i od lewej)
for el in arr:
    f(el)

party(arr)
print("fun: ",f(a))
for i in [a,b,c,d,e,f1,g1,h,i]:
    print(i.name,"\t",i.going,"\t",i.fun,i.f,"\t",i.g,"\t","podwladni: ",len(i.emp))