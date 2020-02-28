class node:                                         #creates nodes
    def __init__(self,data=None):
         self.data = data
         self.next = None
         
class linked_list:
    def __init__(self):
        self.head = node()
    
    def extend(self,data):
        new_node = node(data) 
        cur = self.head

        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    
    def print(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def Ins_First(self,data):
        new_node = node(data)
        if self.head.next == None:
            self.head.next = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
    
    def Ins_Last(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        count = 0
        cur = self.head
        while cur.next != None:
            count = count + 1
            cur = cur.next
        return count
    
    def Ind_Entry(self,index,data):
        new_node = node(data)
        cur = self.head
        for i in range(0,index):
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

Instance = linked_list()
Instance.extend(12)
Instance.extend(15)
Instance.extend(16)
Instance.extend(17)
Instance.extend(18)
Instance.print()
print("Length : ",Instance.length())
Instance.Ind_Entry(4,600)
Instance.print()