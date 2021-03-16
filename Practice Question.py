#Given an element and an array. Check if this element is present in the array or not.
 

 
arr = [5,4,3,6,24,64,3,45,32]
elem = 4
 
for i in arr:
   if i == elem:
       print("present")
       break
else:
   print("not present")
 

 
 
 
 
#Find second largest/ second smallest element in an array ( expected time complexity: O(n), single traversal )
 
 
 
arr1 = [5,4,3,6,24,64,45,32]
max1 = arr1[0]
max2 = arr1[0]
min1 = arr1[0]
min2 = arr1[0]
for i in arr1:
   if i > max1:
       max1 = i
   elif max2!=max1 and max2 < i:
       max2 = i
   elif i < min1:
       min1 = i
   elif min2 != min1 and min2 > i:
       min2 = i
print("Second largest element : ", max2)
print("Second smallest element : ", min2)
 
 
 
 
 
 
 
 
 
 
#Reverse a given array.
 
 
 
 
arr1 = [5,4,3,6,24,64,3,45,32]
arr2 = []
for i in arr1:
   arr2.insert(0,i)
print(arr2)
 
 
