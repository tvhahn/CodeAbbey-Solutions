# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# put the data into integers and in a list
n = list(map(int, f))
n.pop(0) # remove the number of values (first digit)

seed = 113
limit = 10000007

l = len(n)
i = 0
result = 0

while i < l:
    result = ((result + n[i]) * seed) % limit
    i += 1

print(result)