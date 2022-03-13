from Exercises.ex2.mergeTwoSortedLists import merge_lists,printlist,tab2list

def mergeNatSeries(L):
    heads = [L]
    if L.next is None:
        return L

    curr = L.next
    while curr:
        if curr.val >= L.val:
            L = L.next
            curr = curr.next
        else:
            heads.append(curr)
            L.next = None
            L = curr
            curr = curr.next

    heads2 = []
    while len(heads) > 1:
        merged = merge_lists(heads[0], heads[1])
        heads2.append(merged)
        heads = heads[2]
        heads2.extend(heads)
        heads = heads2

    return heads[0]


A = [1, 2, 5, 3, 6, 4, 2, 3, 4, 1, 5]
L = tab2list(A)
mergeNatSeries(L)
printlist(L)