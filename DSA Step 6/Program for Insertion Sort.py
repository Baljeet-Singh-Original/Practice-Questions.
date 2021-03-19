
arr = [1, 2, 3, 4,  5, 6,  7]


###################### If you want to take an input array #####################################

# inp1 = int(input("Enter the length of array : "))
# arr = []
# for i in range(inp1):
#     inp2 = int(input("Enter The Number : "))
#     arr.append(inp2)
# print(arr)

##############################################################################################


insertion = 6
for i in range(1, len(arr)):
    if arr[i] > insertion and arr[i-1] <= insertion:
        arr.insert(i, insertion)
print(arr)

