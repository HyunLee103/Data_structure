""" 링크드 리스트는 결국 파이썬 list()를 만드는 거다. 

    예를 들어, 다음과 같은 리스트가 있을 때
    
    x = [1, 2, 3]
    
    x는 리스트의 첫번째 node 주소값만 가지고 있다.
    
    x[2] 하면 선형 탐색(next를 2번)해서 마지막 노드 주소값을 찾아가 그 안에 value를 return한다
    따라서, 파이썬 리스트는 안에 데이터가 많을 수록 인덱싱 하는 것조차 high cost 하다."""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class Double_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        """ 인스턴스 자체 출력 형식 지정 - instance = linked list
            linked list의 data 값들을 print(instance)로 확인 가능 """
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next
        return res_str
    
    def find_node_at(self, index):
        iterator = self.head
        """ head로 부터 index 만큼 next한 node 반환(주소)
            node.next, node 는 모두 주소/ node.data만 실제 값"""
        for _ in range(index):
            iterator = iterator.next
        
        return iterator
    
    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    """------------ 여기까지 single하고 동일 --------------------"""
    
    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
   
    def insert_after(self,prev_node,data):
        new_node = Node(data)

        if prev_node == self.tail:
            prev_node.next = new_node
            new_node.prev = prev_node
            self.tail = new_node
        else:
            new_node.prev = prev_node
            new_node.next = prev_node.next
            prev_node.next.prev = new_node
            prev_node.next = new_node

    def delete(self, node_to_del):
        data = node_to_del.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node_to_del:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node_to_del:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_del.prev.next = node_to_del.next
            node_to_del.next.prev = node_to_del.prev
        
        return data
             


my_list = Double_LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)
