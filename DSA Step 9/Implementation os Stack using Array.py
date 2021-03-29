    
class stack:
    def __init__(self):
        self.item = []
    def push(self,n):
        self.item.append(n)
        return self.item

    def pop(self):
        if len(self.item) > 0:
            return self.item.pop()
        else:
            print("Stack under flow")
            return False
    def isEmpty(self):
        if not self.item:
            return True
        else:
            return False    
    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)    
