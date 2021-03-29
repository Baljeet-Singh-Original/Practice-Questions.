
arr = []
inp = input("Enter Your Expression : ")
for i in inp:
    arr.append(i)
arr1 = []
opening = ['(','{','[']
closing = [')','}',']']
for i in arr:
    if i in opening:
        arr1.append(i)
    elif (len(arr1) != 0) and (i in closing) and (closing.index(i) == opening.index(arr1[-1])):
        arr1.pop()
    
    
if len(arr1) == 0:
    print('Your Expression is Balanced')
else:
    print('Your Expression is Non Balanced')

    
