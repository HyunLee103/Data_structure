""" 
Tree traversal(트리 순회) : 자료구조에 모든 데이터를 도는 것
                           비선형 자료구조를 데이터 간 선형성을 가지게 해준다.

선형 자료구조와 다르게 tree는 비선형 자료구조이므로 
반복문 대신 재귀함수를 사용한다. 

다음의 동작을 조합하여 순회 방식을 결정한다.

1. 재귀적으로 왼쪽 sub-tree 순회 
2. 재귀적으로 오른쪽 sub-tree 순회
3. 현재 노드 데이터 출력(action)                          
"""

## pre-order(순회 전 action order를 준다) traversal : 3 -> 1 -> 2


## post-order traversal : 1 -> 2 -> 3


## in-order traversal : 1 -> 3 -> 2

class Node:
    """이진 트리 노드를 나타내는 클래스"""

    def __init__(self, data):
        """이진 트리 노드는 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다"""
        self.data = data
        self.left_child = None
        self.right_child = None

def traverse_inorder(node):
    """in-order 순회 함수"""
    if node != None:
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)


## 재귀함수 공부하고 오자..!






