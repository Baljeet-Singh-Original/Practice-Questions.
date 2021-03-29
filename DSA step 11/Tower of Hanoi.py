
def hanoi(n,sr,temp,dest):
    if n == 1:
        print("Move disk %s from %s >>>>>>>>>> %s." %(n,sr,dest))
    else:
        hanoi(n-1,sr,dest,temp)
        print("Move disk %s from %s >>>>>>>>> %s." %(n,sr,dest))
        hanoi(n-1,temp,sr,dest)
        
        
s = 'Source'
t = 'Temp'
d = 'Destination'
a = hanoi(3,s,t,d)
print(a)
