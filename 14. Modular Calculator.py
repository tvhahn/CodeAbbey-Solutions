# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().replace('\n',' ').split(' ')

# function to test if it is a number or symbol
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# function to extract the numbers and symbols and put them in lists
def num_extract(s):
    n = []
    sym = []
    for x in s:
        if is_number(x):
            n.append(int(x))
        else:
            sym.append(str(x))
    return(n, sym)

# tuple unpacking
n, s = num_extract(f)

# run the modular calculator
i = 0
l = len(n)
while i <= (l-1):
    if i == 0:
        ans = n[0]
    elif s[i-1] == '+':
        ans = ans + n[i]
    elif s[i-1] == '*':
        ans = ans * n[i]
    else:
        ans = ans % n[i]
    i += 1

print(ans)