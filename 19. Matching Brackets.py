# open file, get everything on one line, and split the data into a list at the spaces
f = open('nums.txt').read().split('\n')
f.pop(0)

# the types of brackets to extract from a list
brackets = ['<','>','(',')','[',']','{','}']

# great resource that helped me with this problem
# https://stackoverflow.com/questions/2509358/how-to-find-validity-of-a-string-of-parentheses-curly-brackets-and-square-brack

ans = ""

for s in f:
    blist = [x for x in s if x in brackets]
    b1 = blist.count('<')
    b2 = blist.count('>')
    b3 = blist.count('(')
    b4 = blist.count(')')
    b5 = blist.count('[')
    b6 = blist.count(']')
    b7 = blist.count('{')
    b8 = blist.count('}')

    b_str = ""
    for x in blist:
        b_str = b_str + str(x)

    if b1 == b2 and b3 == b4 and b5 == b6 and b7 == b8 and len(blist) % 2 == 0:
        while len(b_str) != 0 and ('<>' in b_str or '()' in b_str or '[]' in b_str or '{}' in b_str):
            b_str = b_str.replace('<>','')
            b_str = b_str.replace('()','')
            b_str = b_str.replace('[]','')
            b_str = b_str.replace('{}','')

        if len(b_str) == 0:
            ans = ans + str(1) + " "
        else:
            ans = ans + str(0) + " "
    else:
        ans = ans + str(0) + " "

print(ans)