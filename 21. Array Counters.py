# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')
f = list(map(int, f))

m = f[0] # length of the array
n = f[1] # N is the range of numbers
del f[:2] # delete the first two numbers

a = [0] * n # create an array of zeros

i = 0
while i < m:
    x = f[i]
    a[x-1] = a[x-1] + 1
    i += 1

ans = ""
for x in a:
    ans = ans + str(x) + " "

print(ans)
