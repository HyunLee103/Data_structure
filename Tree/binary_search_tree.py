"""
이진 탐색 트리(BST)
set, dict 구현에 사용 가능!
binary tree 중, 왼쪽 자식 노드는 부모노드보다 작고, 오른쪽은 큰 tree

탐색 알고리즘을 적용할 때, 위 규칙을 이용해 효율적으로 찾을 수 있다

힙은 complete binary tree라서 파이썬 리스트로 구현 가능했지만
BST는 complete가 보장되지 않기 때문에 node class로 구현한다.

이진탐색트리를 in-order 순회하면 저장된 데이터를 sort해서 출력 가능!

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

"""
각 node가 부모 자식에 대한 reference를 모두 갖고 있다.(doubly linked list 처럼)
"""

node_0 = Node(5)
node_1 = Node(3)
node_2 = Node(7)

node_0.left_child = node_1
node_0.right_child = node_2
node_2.parent = node_0
node_2.parent = node_1

"""
노드 class 말고 이진 탐색트리 class를 다음과 같이 정의해서 만들 수 있다.
"""

def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node != None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_sorted_tree(self):
        print_inorder(self.root)

    def insert(self, data):
        tem = self.root
        new_node = Node(data)

        if self.root == None:
            self.root = new_node
            return
        else:
            while tem is not None: # leaf node 까지만!, leaf의 child는 None이므로 반복이 멈춘다
                if data > tem.data:
                    if tem.right_child == None:
                        new_node.parent = tem
                        tem.right_child = new_node
                        return
                    else:
                        tem = tem.right_child
                
                elif data < tem.data:
                    if tem.left_child == None:
                        tem.left_child = new_node
                        new_node.parent = tem
                        return
                    else:
                        tem = tem.left_child

    def search(self,data):
        tem = self.root

        while tem != None: # leaf node 까지만!, leaf의 child는 None이므로 반복이 멈춘다
            if data == tem.data:
                return tem
            elif data > tem.data:
                tem = tem.right_child
            else:
                tem = tem.left_child
        
        return None

    @staticmethod 
    """
    class instance 속성에 접근 X, instance가 아닌 class 자체에서 바로 호출가능 
    즉, instance 상태를 변화시키지 않는 method를 만들 때 사용
    """
    def find_min(node):
        while node != None:    
            if node.left_child != None:
                node = node.left_child
            else:
                return node



# 빈 이진 탐색 트리 생성
bst = BinarySearchTree()

# 데이터 삽입
bst.insert(7)
bst.insert(11)
bst.insert(9)
bst.insert(17)
bst.insert(8)
bst.insert(5)
bst.insert(19)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(14)

bst.print_sorted_tree()

## 탐색 결과 출력
print(bst.search(19).data)
print(bst.search(20))

## find_min
print(bst.find_min(bst.root.right_child).data)
print(bst.find_min(bst.root).data)

## 데이터 Insert
"""
1. 새 노드 생성
2. root 부터 값을 비교하며 저장할 위치 찾기
3. 찾은 위치에 노드 연결

시간 복잡도 : O(h), h : height of tree
"""

## Search
"""
특정 데이터를 갖는 노드를 return
1. root 부터 탐색 데이터를 비교
2. data > root -> 오른쪽
3. data < root -> 왼쪽
4. 찾을 때 까지 2,3 반복 찾으면 해당 node를 return

시간복잡도 : O(h), h : height of tree
"""







