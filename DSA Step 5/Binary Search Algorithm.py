

arr1 = [1,3,5,7,9,11,13,15,17,19]
def binary(num, arr, index = len(arr1)//2):
    if arr[index]==num:
        return index
    elif num not in arr:
        return ("Not Found")
    elif arr[index] > num:
        return binary(num, arr, index-1)
    else:
        return binary(num, arr, index+1)

print(binary(7, arr1))
