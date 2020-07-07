"""
heap is complete binary tree, 높이가 O(ln(n))
부모 노드 데이터 >= 자식 노드 데이터 
heap은 동적배열, 파이썬에서는 list로 구현할 수 있다.
complete binary tree이므로, 인덱스로 부모, 자식 노드를 찾을 수 있다.

heap 목적
1. heap sort
2. 우선순위 큐 구현
"""

## heapify
""" 부모 노드와 자식 노드를 비교해 힙속성(부모>=자식)에 맞게 재배열 
    O(ln(n)) """

def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    
    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다


tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 


## build heap
""" 리스트로 구현된 완전 이진 트리를 뒤에서 부터 heapify 적용하면 -> heap 
    하나의 노드에 heapify 적용하는 시간복잡도 O(ln(n))이므로, 전체 시간 복잡도는
    O(nln(n)) """

## heap sort 
"""
1. build heap : 위에 참고
for _ in range(index)
    2. root와 마지막 노드 swap
    3. 바꾼 노드는 없는 노드 취급
    4. root가 힙속성을 지킬 수 있게 heapify 호출

시간 복잡도 : O(nln(n))

*내림차순일때는 heapify의 힙속성을 반대로(부모<=자식)
"""

def heapsort(tree):
    tree_size = len(tree)

    for i in range(tree_size,0,-1): # 1. build heap
        heapify(tree,i,tree_size)
    
    for i in range(tree_size-1,0,-1): 
        swap(tree,1,i)              # 2. root, 마지막 노드 swap
        heapify(tree,1,i)           # 4. root에 heapify 호출, tree_size(i)가 줄어들면서 3번 조건 만족시킴

# 실행
data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)



## Priority queue(우선순위 큐)
"""
구현 보다 기능인 추상자료형
데이터의 우선순위를 부여할 수 있고, 해당 순위에 따라 출력 가능
힙으로 구현
"""

## heap에 데이터 삽입
"""
1. 마지막 인덱스에 데이터 삽입
    for _ in range(size):
        2. 삽입 데이터와 부모노드 크기 비교
        3. 부모노드가 작으면 위치 swap

시간 복잡도 : O(ln(n))
"""

def reverse_heapify(tree,index): # heapify 역순으로 밑에서 부터 부모 노드와 비교하며 heapify
    p_index = index//2

    if 0 < p_index < len(tree) and tree[p_index] < tree[index]:
        swap(tree,p_index,index)
        reverse_heapify(tree,p_index)

class PriorityQueue():
    def __init__(self):
        self.heap = [None]

    def insert(self,data):
        self.heap.append(data)
        reverse_heapify(self.heap,len(self.heap)-1)

    def __str__(self):
        return str(self.heap)

# 실행
test = PriorityQueue()

test.insert(6)
test.insert(9)
test.insert(1)
test.insert(10)
test.insert(11)


## 우선순위에 따른 데이터 추출(root 노드 출력(max))
"""
1. root, last swap
2. pop
3. 새로운 root 대상으로 heapify
4. 2단계 pop값 return

시간 복잡도 : O(ln(n))
"""
class PriorityQueue():
    def __init__(self):
        self.heap = [None]

    def insert(self,data):
        self.heap.append(data)
        reverse_heapify(self.heap,len(self.heap)-1)

    def extract_max(self):
        swap(self.heap,1,len(self.heap)-1)
        res = self.heap.pop()
        heapify(self.heap,1,len(self.heap))
        return res

    def __str__(self):
        return str(self.heap)

priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
print(priority_queue.extract_max())
print(priority_queue.extract_max())
print(priority_queue.extract_max())