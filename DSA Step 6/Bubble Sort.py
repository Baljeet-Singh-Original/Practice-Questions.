
arr = [5,4,1,2,3,5,7,2]

################ If you want to take input array ########################

# inp1 = int(input("Enter the length of array : "))    
# arr = []
# for i in range(inp1):
#     inp2 = int(input("Enter The Number : "))
#     arr.append(inp2)

########################################################################

for i in range(len(arr) - 1):
    for j in range(1, len(arr)):
        if arr[j] < arr[j-1]:
            a = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = a

print(arr)
