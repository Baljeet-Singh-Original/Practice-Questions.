
arr1 = [5,4,3,6,24,2,45,32,89]
max1 = arr1[0]
min1 = arr1[0]
for i in arr1:
    if i > max1:
        max1 = i
    elif i < min1:
        min1 = i
print("The largest element is ", max1)
print("The smallest element is ", min1)
