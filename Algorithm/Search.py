""" 탐색 : 저장된 데이터에서 원하는 값을 찾는 것 
    Linear search : 순서대로 하나씩 search
    Binary search : sorted list에 대해서만 중위수를 기준으로 
                    절반씩 범위를 좁혀가는 알고리즘 """

def linear_search(element, some_list):
    for i in range(len(some_list)):    # some_list가 n개의 원소를 가질 때, 반복문이 최대 n번 -> O(n)
        if some_list[i] == element:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))


def binary_search(element, some_list):
    start = 0
    end = len(some_list)-1
    while start <= end:             # 반복문이 최대 ln(n)번 -> O(ln(n))
      
        med = (start+end)//2

        if some_list[med] == element:
            return med
        elif some_list[med] > element:
            end = med -1
        elif some_list[med] < element:
            start = med+1

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))

"""
linear search의 시간 복잡도는 O(n) 이지만, binary search는 O(ln(n))이므로 훨씬 효율적이다.
하지만 B.S는 대상이 sorting 되어 있을때만 적용가능한 제약이 있다.
"""
