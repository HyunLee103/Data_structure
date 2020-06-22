""" Recursion은 base case + recursion case """

## 피보나치 수열
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = F(n-1) + F(n-2)
    return result

for itr in range(0, 10):
    print(F(itr))

## Merge sort
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


## 숫자 합
def sum_num(n):
    if n == 1:
        return 1
    
    return n + sum_num(n-1)

for i in range(1, 11):
    print(sum_num(i))


## 자릿수 합
def sum_digits(n):
    if n < 10:
        return n
    
    return n % 10 + sum_digits(n//10)


# 리스트 뒤집기
def flip(some_list):
    if len(some_list) == 1 or len(some_list) ==  0:
        return some_list
    
    return some_list[-1:] + flip(some_list[:-1])

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)


## BS by recursion
def binary_search(element, some_list, start_index=0, end_index=None):
    if end_index == None:
        end_index = len(some_list) - 1
    
    med = (start_index + end_index)//2

    if some_list[med] == element:
        return med
    elif some_list[med] > element:
        end_index = med - 1 
    else:
        start_index = med + 1
    
    if start_index > end_index:
        return None

    return binary_search(element,some_list, start_index= start_index, end_index=end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))


## 하노이 탑
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    if num_disks == 1:
        return move_disk(num_disks,start_peg,end_peg)

    other_peg = 6 - start_peg - end_peg
    
    hanoi(num_disks-1,start_peg,other_peg)
    move_disk(num_disks,start_peg,end_peg)
    hanoi(num_disks-1,other_peg,end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)
