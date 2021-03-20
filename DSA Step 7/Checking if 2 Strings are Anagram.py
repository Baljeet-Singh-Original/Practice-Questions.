inp1 = input("Enter Your first String : ")
inp2 = input("Enter Your Second String : ")
if len(inp1)==len(inp2):
    for i in inp1:
        if i not in inp2:
            print("Not Anagram")
            break
    else:
        print("Anagram")
