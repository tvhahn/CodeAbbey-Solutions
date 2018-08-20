# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')
f = list(map(int, f))
f.pop(len(f)-1) # remove the last digit (should be -1)

# function to calculate the checksum, as defined in problem 17
def checksum(n):
    seed = 113
    limit = 10000007

    l = len(n)
    i = 0
    result = 0

    while i < l:
        result = ((result + n[i]) * seed) % limit
        i += 1

    return(result)

# function to return array with largest number at end
def bubble_array(n):
    l = len(n)
    i = 0
    counter = 0

    while i<(l-1):
        a = n[i]
        b = n[i+1]
        if a > b:
            n[i+1] = a
            n[i] = b
            counter += 1
            i += 1
        elif a < b:
            i += 1
        else:
            i +=1

    ans = checksum(n)
    return(counter, ans)

count, ans = bubble_array(f)

print(count,ans)