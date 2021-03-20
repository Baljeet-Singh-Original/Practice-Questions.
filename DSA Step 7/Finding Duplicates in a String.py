inp = input("Enter Your String Here : ")
string1 = ''
for i in inp:
    if i not in string1:
        string1 +=i
    else:
        print("Your Duplicates : ", i)
