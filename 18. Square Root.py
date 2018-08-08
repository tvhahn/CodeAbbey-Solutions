# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# put the data into integers and in a list
n = list(map(int, f))
n.pop(0) # remove the number of values (first digit)


l = len(n)
i = 0
ans = ""

while i < l:
    X = n[i] # value that we want to calculate sqr root for
    N = n[i+1] # steps to perform for approximation
    step = 1 # step counter
    r = 1 # initial guess for sqr root

    while step <= N:
        d = X / r
        avg = (d + r) / 2
        r = avg
        step += 1

    ans = ans + str(r) + " "
    i += 2

print(ans)