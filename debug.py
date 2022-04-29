class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class singlyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:  # means that linked list has no element
            self.head = new_node
        else:
            temp = self.head
            while not temp.next == None:
                temp = temp.next
            temp.next = new_node

    def print_linkedList(self):
        if self.head is None:
            print("linded list is empty")
        else:
            temp = self.head
            while not temp == None:
                print(temp.data, end=" ")
                temp = temp.next

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            tempNode = Node(data)
            tempNode.next = self.head
            self.head = tempNode

    def insertAfterNode(self, value, data):  # insert by value
        if self.head is None:
            print("list is empty")
        else:

            insertNode = Node(data)
            tempNode = self.head
            while True:
                if value != tempNode.data:
                    tempNode = tempNode.next
                else:
                    insertNode.next = tempNode.next
                    tempNode.next = insertNode
                    break

    def deleteNodebyValue(self, value):
        if self.head is None:
            raise("linked list is empty")
        else:
            tempNode = self.head
            while True:
                if tempNode.next.data != value:
                    tempNode = tempNode.next
                else:
                    nextNode = tempNode.next.next
                    del tempNode.next.next
                    tempNode.next = nextNode
                    break

    def deleteByPos(self, key):
        if key < 0:
            raise("key must be zero or bigger")
        elif(key == 0):
            temp = self.head.next
            del self.head
            self.head = temp
            del temp
        else:
            count = 0
            tempNode = self.head
            while count < key - 1:  # to land one node before the node that should be deleted
                tempNode = tempNode.next
                count = count + 1
            temp = tempNode.next.next
            tempNode.next.next = None
            tempNode.next = temp
            del temp

    def length(self):
        def _len_rec(node):
            if node is None:
                return 0
            return 1 + _len_rec(node.next)
        return _len_rec(self.head)

    def swapNode(self, key_1, key_2):
        """_summary_

        Args:
            key_1 (int): _1st node pos_
            key_2 (int): _2nd node pos_
        """

        if key_1 == key_2:
            return

        nodeKey_1 = key_1 if key_1 < key_2 else key_2
        nodeKey_2 = key_2 if key_2 > key_1 else key_1

        if nodeKey_1 == 0:
            curr_1 = self.head

            index = 2
            prev_2 = curr_1.next
            while index < nodeKey_2:
                prev_2 = prev_2.next
                index += 1

            curr_2 = prev_2.next  # here we know that curr_2 is prev_2.next

            """
            in this if statment we have initialized curr_1, prev_2 and curr_2 since curr_1 is the head we dont have prev_1
            """
            #first node is the head
            temp = curr_2.next

            self.head = curr_2
            prev_2.next = curr_1
            curr_2.next = curr_1.next
            curr_1.next = temp

        else:
            prev_1 = self.head
            index = 1
            while index < nodeKey_1:
                prev_1 = prev_1.next  # stops one node before the target Node
                index += 1

            curr_1 = prev_1.next

            prev_2 = curr_1  # continue linkedList where we left in the first while loop
            index += 1  # move one index up
            while index < key_2:
                prev_2 = prev_2.next
                index += 1

            curr_2 = prev_2.next  # initializing curr_2

            """
            in else function we have 4 nodes: prev_1 , curr_1, prev_2, curr_2
            """

            if curr_1.next == curr_2:

                temp = curr_2.next
                prev_1.next = curr_2
                curr_2.next = curr_1
                curr_1.next = temp

            else:

                temp = curr_2.next          # temp to store the address of the curr_2.next
                prev_1.next = curr_2        # perv_1 now points to curr_2
                curr_2.next = curr_1.next   # curr_2.next now points to curr_1.next

                prev_2.next = curr_1        # prev_2.next now point to curr_1
                curr_1.next = temp  # curr_1.next points to temp which is address of curr_2.next

    def reverseLinkList(self):

        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverselinklistRecursivly(self):
        prev = None
        curr = self.head

        def _recursive_reversing(prev, curr):

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            if(curr):
                _recursive_reversing(prev, curr)
            else:
                self.head = prev
        _recursive_reversing(prev, curr)

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def mergeTwoSortedLinkLists(self, listHeadA, listHeadB):
        pointerA = listHeadA.head
        pointerB = listHeadB.head

        while pointerA and pointerB:
            valueInA = pointerA.data
            valueInB = pointerB.data

            if(valueInA < valueInB):
                self.append(valueInA)
                pointerA = pointerA.next
            else:
                self.append(valueInB)
                pointerB = pointerB.next
        if(pointerB and not pointerA):
            while pointerB:
                self.append(pointerB.data)
                pointerB = pointerB.next
        elif(pointerA and not pointerB):
            while pointerA:
                self.append(pointerA.data)
                pointerA = pointerA.next

    def extendlinkList(self, listB):
        """_summary_

        Args:
            listB (_linkedlist_): _ list B to be merged with list A._

        Returns:
            _linkList_: _ merges the two list a and b and return a head for the orginal list _
        """
        curr = self.head
        ptrB = listB.head
        c = None

        if not curr:
            return ptrB
        if not ptrB:
            return curr

        if curr and ptrB:

            if curr.data <= ptrB.data:
                c = curr
                curr = c.next
            else:
                c = ptrB
                ptrB = c.next

            newHead = c

        while curr and ptrB:

            if curr.data <= ptrB.data:
                c.next = curr
                c = curr
                curr = c.next
            else:
                c.next = ptrB
                c = ptrB
                ptrB = c.next

        if curr and not ptrB:
            c.next = curr

        if ptrB and not curr:
            c.next = ptrB

        self.head = newHead

        return self.head

    def removeDublicate(self):
        curr = self.head
        prev = None
        dub_values = dict()

        while curr:

            if curr.data in dub_values:
                #remove the node
                prev.next = curr.next
                curr.next = None
                curr = None
            else:
                #if the value dos'nt exsits add that to dic
                dub_values[curr.data] = 1
                prev = curr
            curr = prev.next

    def moveNodeToLast(self, pos):
        #my solution 
        curr = self.head
        nodePos = pos
        prev = None
        lastNodePrev = None
        lastNodePos = self.length() - 1

        if nodePos >= lastNodePos:
            return
        
        elif nodePos == 0: #target node is the head
            
            i = 0
            while curr.next:  # finiding one-node-before-last
                lastNodePrev = curr
                curr = curr.next
            temp = self.head
            self.head = lastNodePrev.next  # to re assign the self.head to new head
            lastNodePrev.next.next = temp.next
            lastNodePrev.next = temp
            temp.next = None  
        else:
                i = 0
                while curr.next:
                    if i < nodePos:
                        prev = curr
                        i = i + 1

                    lastNodePrev = curr
                    curr = curr.next

                #swapping the element with the last node
                temp = prev.next  # temp is the target Node                

                if temp.next.next == None:  # we check if we replacing the one-node-before-last
                    prev.next = lastNodePrev.next
                    lastNodePrev.next.next = lastNodePrev
                    lastNodePrev.next = None  # it becomes last element
                else:
                    prev.next = lastNodePrev.next
                    lastNodePrev.next.next = temp.next
                    lastNodePrev.next = temp
                    temp.next = None
    
    def print_nthNode_fromLast(self,n):
        lastNodePos = self.length()
        curr = self.head
        while curr:
            if lastNodePos == n:
                print (curr.data)
                return curr.data
            else:
                curr = curr.next
                lastNodePos -=1
                if lastNodePos == 0:
                    print("None")
                    return None

    def count_occurrence(self):
        curr = self.head
        occurrence = dict()
        def _recursive_itr(node):
            if node == None:
                return 
            else:
                occurrence.update({node.data: occurrence.get(node.data,0) + 1})
                node = node.next
                _recursive_itr(node)
                
        _recursive_itr(curr)
        dictView = occurrence.items()
        print(dictView)




l_1 = singlyLinkedList()
l_1.append(4)
l_1.append(5)
l_1.append(6)
l_1.append(4)
l_1.append(7)
l_1.append(8)
l_1.append(8)
l_1.append(8)
l_1.append(9)

print()
l_1.print_linkedList()
print()
l_1.count_occurrence()
