
arr = [2, 4, 5, 7, 8, 10] 
k=11
arr1 = []
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==k and arr[i] not in arr1:
            print([arr[i], arr[j]])
            arr1.append(arr[i])
            arr1.append(arr[j])
            
