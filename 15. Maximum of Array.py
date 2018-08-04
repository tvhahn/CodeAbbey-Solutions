# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

n = list(map(int, f))

# function to find the min and max in a list
def min_max(s):
    l = len(s)
    i = 0
    min = s[0]
    max = s[0]
    while i < l:
        if s[i] == s[i-1]:
            pass
        elif s[i] > max:
            max = s[i]
        elif s[i] < min:
            min = s[i]

        i += 1

    return(min, max)

min, max = min_max(n)

print(str(max)+" "+str(min))