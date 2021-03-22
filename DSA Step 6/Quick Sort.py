def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high]
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )
def quickSort(arr,low,high):
   if low < high:
      pi = partition(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

###################### If you want to take an input array #####################################

# inp1 = int(input("Enter the length of array : "))
# arr = []
# for i in range(inp1):
#     inp2 = int(input("Enter The Number : "))
#     arr.append(inp2)
# print(arr)

##############################################################################################

arr = [2,5,3,8,6,5,4,7]
n = len(arr)
quickSort(arr,0,n-1)
print (arr)
