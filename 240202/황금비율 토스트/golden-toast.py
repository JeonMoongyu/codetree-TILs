class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    
    def push_back(self, new_data):  
        if self.begin() == self.end():  # self.head == self.tail, that is, dll is empty
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev = new_node
            
    
    def erase(self, node):
        next_node = node.next
        if node == self.begin():
            node.next.prev = None    
            self.head = node.next
            node.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None
        return next_node


    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        elif node == self.begin():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
            
            
    def begin(self):
        return self.head
        
    
    def end(self):
        return self.tail
        
        
n, m = tuple(map(int,input().split()))
string = input()
l = DoublyLinkedList()

for letter in string:
    l.push_back(letter)

it = l.end()

for _ in range(m):
    com = input()
    if com == 'L':
        if it == l.begin():
            continue
        it = it.prev
    elif com == 'R':
        if it == l.end():
            continue
        it = it.next
    elif com == 'D':
        if it == l.end():
            continue
        it = l.erase(it)
    else: # com[0] == 'P':
        letter = com[2]
        l.insert(it, letter) 

it = l.begin()
while it != l.end():
    print(it.data, end="")
    it = it.next