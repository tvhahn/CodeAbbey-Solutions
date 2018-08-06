# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().split('\n')
f.pop(0)

l = len(f)
i = 0
s = " "

while i < l:
    a = list(f[i].split(' '))
    b = list(map(int,a))
    avg = round(sum(b)/(len(b)-1))
    s += str(avg)+" "
    i += 1

print(s)
