
a = [0,1,1]
b = [0,1,2]

# a = [ -5, 7, -12, 4, -6, 2, -5, -12, -6, 3, 11, 10, -8, 11, -13, -8, 5, -12, 4, 4 ]
# b = [ -6, 6, -8, -13, -2, -9, -10, -10, -7, -14, 9, -8, -4, 8, 13, -11, 13, 5, 9, 11 ]

ans = 0
for i in range(1, len(a)):
    ans += max(abs(a[i-1] - a[i]), abs(b[i-1]-b[i]))

print(ans)