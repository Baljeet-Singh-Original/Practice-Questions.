
inp=input("Enter Your Word : ")
pal =""
for i in inp:
    pal= i+pal

if inp==pal:
    print("It's a palindrome")
else:
    print("it's not a palindrome.")
