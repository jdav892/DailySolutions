class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def push(head, data):
        n = Node(data)
        n.next = head
        return n
    
    def build_one_two_three():
        return push(push(Node(3), 2), 1)