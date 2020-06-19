# 피보나치 수열
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = F(n-1) + F(n-2)
    return result

for itr in range(0, 10):
    print(F(itr))

# Merge sort
import random

def Mergesort(lstTosort):
    if len(lstTosort) == 1:
        return lstTosort
    
    sub_lstTosort1 = []
    sub_lstTosort2 = []

    for itr in range(len(lstTosort)):
        if len(lstTosort)/2 > itr:
            sub_lstTosort1.append(lstTosort[itr])
        else:
            sub_lstTosort2.append(lstTosort[itr])
    
    sub_lstTosort1 = Mergesort(sub_lstTosort1)
    sub_lstTosort2 = Mergesort(sub_lstTosort2)

    idx1 = 0
    idx2 = 0

    for itr in range(len(lstTosort)):
        if idx1 == len(sub_lstTosort1):
            lstTosort[itr] = sub_lstTosort2[idx2]
            idx2 += 1
        elif idx2 == len(sub_lstTosort2):
            lstTosort[itr] = sub_lstTosort1[idx1]
            idx1 += 1
        elif sub_lstTosort1[idx1] > sub_lstTosort2[idx2]:
            lstTosort[itr] = sub_lstTosort2[idx2]
            idx2 += 1
        else:
            lstTosort[itr] = sub_lstTosort1[idx1]
            idx1 += 1
    return lstTosort

lst = []

for itr in range(0,10):
    lst.append(random.randrange(0,100))

print(lst)

lst = Mergesort(lst)

print(lst)

