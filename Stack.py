class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = node()
    
    def push(self,data):
        new_node = node(data)
        if self.head.next == None:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
    
    def pop(self):
        current = self.head.next
        self.head = self.head.next
        info = current.data
        del current
        return info

    def print(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)




