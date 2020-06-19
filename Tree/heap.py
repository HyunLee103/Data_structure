"""
heap is complete binary tree, 높이가 O(ln(n))
부모 노드 데이터 >= 자식 노드 데이터 
heap은 동적배열, 파이썬에서는 list로 구현할 수 있다.
complete binary tree이므로, 인덱스로 부모, 자식 노드를 찾을 수 있다.
"""

# heapify
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
    
    if tree[index] < tree[left_child_index]:
        swap(tree,index,left_child_index)
    elif tree[index] < tree[right_child_index]:
        swap(tree,index,right_child_index)


tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree) 



