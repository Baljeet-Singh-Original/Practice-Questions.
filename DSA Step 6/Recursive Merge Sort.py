

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1


arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]


###################### If you want to take an input array #####################################

# inp1 = int(input("Enter the length of array : "))
# arr = []
# for i in range(inp1):
#     inp2 = int(input("Enter The Number : "))
#     arr.append(inp2)
# print(arr)

##############################################################################################


mergeSort(arr)
print(arr)
