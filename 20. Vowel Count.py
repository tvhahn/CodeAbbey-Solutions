# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().split('\n')
f.pop(0)

# list of vowels
vowels = ['a','o','u','i','e','y']

ans = ""

for s in f:
    v_list = [x for x in s if x in vowels]
    ans = ans + str(len(v_list)) + " "

print(ans)