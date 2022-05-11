class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = Node(data)
            curr.next.prev = curr
        else:
            self.head = Node(data)
    
    def prepend(self,data):
        if self.head:
            curr = self.head 
            curr.prev = Node(data)
            curr.prev.next = curr
            self.head = curr.prev
        else:
            self.head = Node(data)
    
    def printList(self):
        curr = self.head
        print()
        while curr:
            print(curr.data, end =" ")
            curr = curr.next
        print()
    def insert_node_after(self,key,data):
        if self.head:
            curr = self.head
            while curr:
                if curr.data == key:
                    if curr.next:
                        temp = curr.next
                        curr.next = Node(data)
                        temp.prev = curr.next
                        curr.next.next = temp
                        return 
                    else:
                        curr.next = Node(data)
                        curr.next.prev = curr
                        return 
                else:
                    curr = curr.next

    def insert_node_before(self,key,data):
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.prev:                       # 1   4 
                    curr.prev.next = Node(data)     # 1   4     2
                    curr.prev.next.next = curr
                    curr.prev.next.prev = curr.prev
                    break
                else:
                    # it means that it is the head
                    curr.prev = Node(data)
                    curr.prev.next = curr
                    self.head = curr.prev
                    break 
            else:
                curr = curr.next
    def delete(self,key):
        # case_1: target Node is head
        # case_2: target Node is tail
        # case_3: target Node dose'nt exist
        # case_4: target Node is Nth node
        curr = self.head
        while curr:
            if curr.data == key:
                if curr.next:
                    if curr.prev: # target Node is Nth node
                        curr.prev.next = curr.next
                        curr.next.perv = curr.prev
                        curr.next = None
                        curr.prev = None
                        return
                    else: # node target is head
                        self.head = curr.next
                        curr.next = None
                        return
                else: #node target is tail
                    curr.prev.next = None
                    curr.perv = None
                    return 
            else:
                curr = curr.next       
    def reverse_recursivly(self):
        curr = self.head
        def _recursive(node):
            if node.next:
                pre = node
                nextNode = node.next

                pre.prev = nextNode
                pre.next = nextNode.next
                nextNode.next = pre
                nextNode.prev = pre.prev
                _recursive(nextNode)

            else:
                self.head = node
                return
        _recursive(curr)

d_1 = DoublyLinkList()
d_1.prepend(0)
d_1.append(1)
d_1.append(2)
d_1.append(3)
d_1.append(4)
d_1.append(14)
d_1.prepend(5)
d_1.prepend(10)

d_1.printList()
d_1.reverse_recursivly()
d_1.printList()
