# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')
f = list(map(int, f))
f.pop(0) # remove the number of values (first digit)

l = len(f)
ans =""

i = 0
while i < l:
    x = f[i]
    y = f[i+1]
    n = f[i+2]

    a = int(y * n / (x + y))
    b = int(x * n / (x + y))

    ans1 = int(max((a + 1) * x, b * y))
    ans2 = int(max(a * x, (b + 1) * y))

    ans = min(ans1, ans2)
    print(ans, end = ' ')
    i += 3