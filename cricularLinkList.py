class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLink:
    def __init__(self):
        self.head = None

    def append (self, data):
        if self.head:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = Node(data)
            curr.next.next = self.head
        else:
            self.head = Node(data)
            self.head.next = self.head
    
    def prepend (self,data): #make the new element head of the linkList
        if self.head:
            tail = self.head
            while tail:
                if tail.next == self.head:
                    break
                tail = tail.next
            newNode = Node(data)
            tail.next = newNode
            newNode.next = self.head
            self.head = newNode
        else: 
            self.append(data)
            
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data , end =" ")
            curr = curr.next
            if curr == self.head:
                break
    def removeNode(self,key): # we will remove the first occurrence of the key node
        if self.head:
            curr = self.head
            preTarget=None
            while curr:
                if curr.data == key:
                    break
                preTarget = curr
                curr = curr.next
                if curr == self.head:
                    break
            if preTarget:
                preTarget.next = curr.next
                curr.next = None
            else:
                if curr == self.head and curr.next == self.head: # in circular list means that list has only one node
                    print("list is empty")
                    self.head = None
                    return
                else:# for link-list with more than one nodes
                    tail = None
                    while curr:
                        curr = curr.next
                        if curr == self.head:
                            break
                        tail = curr
                    #since Pretarget is None that means the key is the first node which is the head
                    target = self.head
                    tail.next = target.next
                    self.head = target.next
                    target = None
        else:
            raise("node is empty")
    #@overload
    def __len__(self)->int:
        if self.head:
            count = 0
            curr = self.head
            while curr:
                count += 1
                curr = curr.next
                
                if curr == self.head:
                    break
            return count
        else:
            return 0
    
    def splitLink(self):
        # ***
        # this function split the orginal link-list into two halves 
        # retuns the head pointer of the second link-list
        # ***
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        # 1 2 3  4 5 6 7
        mid = len(self)//2
        currentPos = 1
        head_1 = self.head
        tail_1 = None
        head_2 = None       
        tail_2 = None
        curr = self.head
        while curr:
            if currentPos == mid:
                tail_1 = curr
                head_2 = curr.next
            tail_2 = curr
            curr = curr.next
            currentPos +=1
            if curr == self.head: #which means 
                break
        # we now initiallezd all the pointers with the correct addresses 
        tail_1.next = head_1
        tail_2.next = head_2
        return head_2
    
    def remove(self,node):
        curr = self.head
        if node == self.head:
            while curr:
                curr = curr.next
                if curr.next == self.head:
                    break
            curr.next = self.head.next
            self.head = self.head.next
        else:
            pre = None
            while curr:
                pre = curr
                curr = curr.next
                if curr == node:
                    break
            pre.next = curr.next
            curr.next = None
           


    def josephus_circle(self,step):
        curr = self.head
        count = 1

        while curr:
            if curr == curr.next:
                break
            if count == step:
                print("kill node :" + str(curr.data))
                temp = curr
                curr = curr.next
                self.remove(temp)
                count = 1
            count +=1
            curr = curr.next
            # print(curr.data)

        if self.head == self.head.next:
            self.head.next = None
            print("winner " + str(self.head.data))
            return self.head.data


                
         

c_1 = CircularLink()
c_2 = CircularLink() # now c_2.head == None

c_1.append(5)
c_1.append(10)
c_1.append(15)
c_1.append(20)
c_1.append(25)
c_1.printList()
# print("after splliting")
# c_2.head = c_1.splitLink() #assign the c_2.head to the second list's head
# c_1.printList()
print()
c_1.josephus_circle(3)
c_1.printList()
