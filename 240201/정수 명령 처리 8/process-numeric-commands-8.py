class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = self.head
        
        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.node_num += 1
        
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        new_node.next = None
        
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.node_num += 1
    
    
    def pop_front(self):
        if self.node_num == 0: 
            print("List is empty")
        elif self.node_num == 1:
            ex_head = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            return ex_head.data
        else:
            ex_head = self.head
            ex_head.next.prev = None
            self.head = ex_head.next
            ex_head.next = None
            self.node_num -= 1
            return ex_head.data
    
    
    def pop_back(self):
        if self.node_num == 0:
            print("List is empty")
        elif self.node_num == 1:
            ex_tail = self.tail
            self.head = None
            self.tail = None
            self.node_num = 0
            return ex_tail.data
        else:
            ex_tail = self.tail
            ex_tail.prev.next = None
            self.tail = ex_tail.prev
            ex_tail.prev = None
            self.node_num -= 1
            return ex_tail.data
            
    
    def size(self):
        return self.node_num
    
    
    def empty(self):
        return self.node_num == 0
    
    
    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            return self.head.data
    
    
    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            return self.tail.data


n = int(input())
dll = DoublyLinkedList()

for _ in range(n):
    command = list(input().split())
    command0 = command[0]
    if command0 == "push_front":
        a = int(command[1])
        dll.push_front(a)
    elif command0 == "push_back":
        a = int(command[1])
        dll.push_back(a)
    elif command0 == "pop_front":
        print(dll.pop_front())
    elif command0 == "pop_back":
        print(dll.pop_back())
    elif command0 == "size":
        print(dll.size())
    elif command0 == "empty":
        if dll.empty():
            print(1)
        else:
            print(0)
    elif command0 == "front":
        print(dll.front())
    elif command0 == "back":
        print(dll.back())