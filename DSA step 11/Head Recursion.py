
def headRec(n):
    if n == 0:
        return n
    else:
        headRec(n-1)
    print(n)
    
headRec(5)
