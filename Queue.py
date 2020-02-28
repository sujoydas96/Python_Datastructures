class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = node()
    
    def insert(self,data):
        new_node = node(data)
        if self.head.next == None:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def print(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)
    
    def remove(self):
        cur = self.head
        prev = self.head
        while cur.next != None:
            prev = cur
            cur = cur.next
        prev.next = None
        info = cur.data
        del cur
        return info

