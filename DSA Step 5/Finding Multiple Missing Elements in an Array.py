
arr = [ 6, 7, 10, 11, 13 ]

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]+1:
        a=arr[i]-arr[i-1]
        for j in range(1, a):
            print(arr[i-1]+j)
