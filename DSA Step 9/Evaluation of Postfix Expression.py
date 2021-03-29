
def eval(arr):
    stack = []
    operators = ["+","-","*","/","%"]
    
    for item in arr:
        if item not in operators:
            stack.append(item)
        else:
            first = int(stack.pop())
            sec = int(stack.pop())
            
            if item == "+":
                stack.append(sec + first)
            if item == "-":
                stack.append(sec - first)
            if item == "*":
                stack.append(sec * first)
            if item == "/":
                stack.append(sec / first)
            if item == "%":
                stack.append(sec % first)
    return stack[-1] 

a = ["2","1","+","3","*"]   
print(eval(a))
