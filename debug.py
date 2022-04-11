"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        
        self.items = []
        
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def getLength(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == list()
    
    def getStack(self):
        return self.items


def is_mathced(string):
    if string == "{}":
        return True
    elif string == "()":
        return True
    elif string == "[]":
        return True
    else:
        return False



def is_paren_balanced(string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(string) and is_balanced:
        if(string[index] in "({["):
            s.push(string[index])
            index = index + 1
        else:
            if(s.isEmpty()):
                if(index <= len(string) -1 ):
                    is_balanced = False
                    break
            else:
                top = s.pop()
              
                op = top+string[index]
                
                if is_mathced(op): 
                    index =  index + 1
                    if(index >= len(string) and not s.isEmpty()):
                        is_balanced = False
                        break
                else:
                    is_balanced = False
                    break
    if(not s.isEmpty() and index == len(string)):
        is_balanced = False

                
    return is_balanced
            

print(is_paren_balanced("{(})}")) 
