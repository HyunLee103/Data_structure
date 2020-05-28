## Node 생성
class Node:
    def __init__(self,data):
        self.data = data # 노드에 저장 할 값
        self.next = None # 다음 노드에 대한 reference
        
## Node instance 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

## 생성 된 Node 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

## Node value 값들 출력
iterator = head_node
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

## linked list 생성
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_after(self,prev_node,data):
        new_node = Node(data)

        if prev_node == self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node
    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def del_after(self, prev_node):
        
        data = prev_node.next.data # linked list 삭제한 데이터가 어떤 건지 return 해주는 게 국룰

        if prev_node.next is self.tail:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = prev_node.next.next

        return data
    
    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        data = self.head.data
        
        self.head = self.head.next
        if self.head == None:
            self.tail = None

        return data

    def find_node_at(self, index):
        iterator = self.head
        """ head로 부터 index 만큼 next한 node 반환(주소)
            node.next, node 는 모두 주소/ node.data만 실제 값"""
        for _ in range(index):
            iterator = iterator.next
        
        return iterator

    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

    def __str__(self):
        """ 인스턴스 자체 출력 형식 지정 - instance = linked list
            linked list의 data 값들을 print(instance)로 확인 가능 """
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next
        return res_str

## linked list instance를 만들고, append method 이용해, data 저장
my_list = Linkedlist()
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)
my_list.head.next.data
my_list.del_after(my_list.head)
## Access Linked List
""" linked list는 node 간 reference로 다음 node에 접근이 가능하므로
한번에 i번째 node에 접근하는 것은 불가능 하고 head 부터 i번 reference(next)를 통해
접근해야한다"""
print(my_list.find_node_at(3).data)
my_list.find_node_at(2).data = 13
print(my_list)


node_2 = my_list.find_node_at(2) # index 2 node 접근
my_list.insert_after(node_2, 6) # index 2 node(prev) 뒤에 6 insert
print(my_list)

head = my_list.head
my_list.insert_after(head,128)
print(my_list)