
arr = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

###################### If you want to take an input array #####################################

# inp1 = int(input("Enter the length of array : "))
# arr = []
# for i in range(inp1):
#     inp2 = int(input("Enter The Number : "))
#     arr.append(inp2)
# print(arr)

##############################################################################################


arr1 = []
for i in range(max(arr)):
    arr1.append(0)
for i in arr:
    arr1[i-1] += 1
arr2 = []

for i in range(len(arr1)):
    if arr1[i]==0:
        pass
    else:
        for j in range(arr1[i]):
            arr2.append(i+1)
print(arr2)
