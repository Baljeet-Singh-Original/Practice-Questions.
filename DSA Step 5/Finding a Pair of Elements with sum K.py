
arr = [5,4,1,2,3,5,7,2]
k=8
for i in arr:
    for j in range(1, len(arr)-1):
        if i+arr[j]==k and i != arr[j]:
            print([i, arr[j]])
