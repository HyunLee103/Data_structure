"""
tree : 데이터의 계층적(상하) 관계를 나타내는 자료구조
array, list는 선형 구조라 이런 관계를 표현할 수 없음
정렬, 압축 등에 효과적임
딕셔너리, 세트, 큐 등 추상자료형을 구현 가능하다.
"""

## binary tree : 모든 노드의 최대 노드가 2개인 tree 

# Node class 선언
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# node instance 생성
root_node = Node(2)
node_B = Node(3)
node_C = Node(5)
node_D = Node(7)
node_E = Node(11)

# instance 간 tree 구조로 reference 연결
root_node.left_child = node_B
root_node.right_child = node_C
node_B.left_child = node_D
node_B.right_child = node_E

# result
root_node.left_child.data
node_B.right_child.data

# quiz
root = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_G = Node('G')
node_H = Node('H')
node_F = Node('F')

root.left_child = node_B
root.right_child = node_C
node_B.right_child = node_E
node_B.left_child = node_D
node_E.left_child = node_G
node_E.right_child = node_H
node_C.right_child = node_F

## complete binary tree
""" 파이썬 리스트로 cbt를 구현할 수 있다 
    특정 노드의 left는 idx * 2 , right는 idx * 2 + 1
    부모 노드는 자식 노드 idx/2  """

def get_parent_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    idx = index//2
    if complete_binary_tree[idx]:
        return idx
    else:
        return None

def get_left_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    idx = index * 2
    if 0 <= idx <= len(complete_binary_tree):
        return idx
    else:
        return None

def get_right_child_index(complete_binary_tree, index):
    """배열로 구현한 완전 이진 트리에서 index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    idx = (index * 2) + 1
    if 0 <= idx <= len(complete_binary_tree):
        return idx
    else:
        return None

root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)

