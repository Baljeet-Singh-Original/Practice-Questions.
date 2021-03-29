
class stack:
    def __init__(self):
        self.item = []
    def push(self,data):
        self.item.insert(0,data)
        return self.item
    def isEmpty(self):
        return self.item == []
    def pop(self):
        return self.item.pop(0)
    def peek(self):
        return self.item[0]
    def size(self):
        return len(self.item)

def infinixToPostfix(inex):
    pr = {}
    pr["^"] = 4
    pr["/"] = 3
    pr["*"] = 3
    pr["+"] = 2
    pr["-"] = 2
    pr["("] = 1
    
    opstck = stack()
    postfix = []
    tokenlist = inex.split()
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "abcdefghijklmnopqrstuvwxyz":
            postfix.append(token)
        elif token == "(":
            opstck.push(token)
        elif token == ")":
            topToken = opstck.pop()
            while topToken != "(":
                postfix.append(topToken)
                topToken = opstck.pop()
        
        else:
            while (not opstck.isEmpty()) and (pr[opstck.peek()] >= pr[token]):
                postfix.append(opstck.pop())
            opstck.push(token)

    while not opstck.isEmpty():
        postfix.append(opstck.pop())
    return " ".join(postfix)

k = input("Enter Your Expression : ")  # "A * B - ( C + D ) + E"
print(infinixToPostfix(k))
