""" 순서가 없는 데이터는 배열 형태로 저장할 필요없다
    대신 key : value 사용 """

""" 해시 함수 : 특정 값을 원하는 범위의 자연수로 변환 """

""" 해시 테이블 : 배열 + 해시 함수, key 값을 해시함수를 통해 일정 범위의 값으로 변환한 뒤, 
    그 값의 배열 인덱스에 key : value를 저장"""

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_with_key(self, key):
        iterator = self.head

        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator += iterator.next

        return None
    
    def append(self, key, value):
        new_node = Node(key, value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def delete(self, node_to_del):
        if node_to_del == self.head and node_to_del == self.tail:
            self.head = None
            self.tail = None

        elif node_to_del == self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_del == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:
            node_to_del.prev.next = node_to_del.next
            node_to_del.next.prev = node_to_del.prev

    def __str__(self):
        res_str = ""

        iterator = self.head

        while iterator != None:
            res_str += "{} : {}".format(iterator.key, iterator.value)
            iterator = iterator.next

        return res_str

class Hash_table:
    def __init__(self, capacity):
    """ capacity 길이의 리스트를 만들고 각 리스트에 빈 Linkedlist가 저장"""
        self._capacity = capacity
        self._table = [Linkedlist() for _ in range(self._capacity)]

    def _hash_f(self, key):
        return hash(key) % self._capacity

    def __str__(self):
        res_str = ""

        for linked_list in self._table:
            res_str = str(linked_list)

        return res_str[:-1]
    
    ## key -> hash 해당하는 인덱스의 linked list 반환
    def _get_linkedlist_for_key(self, key):
        hashed_index = self._hash_f(key)

        return self._table[hashed_index]

    ## 특정 key를 갖는 node 반환    
    def _look_up_node(self, key):
        linked_list = self._get_linkedlist_for_key(key)

        return linked_list.find_node_with_key(key)

    ## 해시 테이블 탐색
    def look_up_value(self, key):
        
        return self._look_up_node(key).value

    ## 해시 테이블 삽입
    def insert(self, key, value):
        
        exist_node = self._look_up_node(key)

        if exist_node is None:
            self._get_linkedlist_for_key(key).append(key, value)
        else:
            self._look_up_node(key).value = value

    ## 해시 테이블 삭제
    def delete_by_key(self, key):

        exist_node = self._look_up_node(key)

        if exist_node in None:
            return None
        else:
            self._get_linkedlist_for_key(key).delete(exist_node)
