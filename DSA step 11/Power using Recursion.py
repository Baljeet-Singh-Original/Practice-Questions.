
def power(N, P):
    
    if P == 0 or P == 1 :
        return N
    else:
        return (N*power(N, P-1))
    
