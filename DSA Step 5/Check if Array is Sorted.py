
arr1 = [1,3,5,7,9,11,13,15,17,19]

for i in range(1, len(arr1)):
    if arr1[i] < arr1[i-1]:
        print("Not Sorted on" , i-1 , "th index")
