
def tailRec(n):
    if n == 0:
        return n
    else:
        print(n)
    tailRec(n-1)
    
tailRec(5)
